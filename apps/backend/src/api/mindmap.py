from fastapi import APIRouter, Depends, HTTPException, WebSocket
from sqlalchemy.orm import Session
from typing import List, Optional

from ..core.security import get_current_user
from ..core.database import get_db
from ..models.mindmap import MindMap, Node, Connection
from ..services.ai_service import AIService
from ..services.mindmap_service import MindMapService
from ..schemas.mindmap import (
    MindMapCreate,
    MindMapUpdate,
    MindMapResponse,
    NodeCreate,
    NodeUpdate,
    NodeResponse
)

router = APIRouter()
ai_service = AIService()
mindmap_service = MindMapService()

@router.post("/mindmaps/", response_model=MindMapResponse)
async def create_mindmap(
    mindmap: MindMapCreate,
    current_user = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Create a new mind map"""
    return mindmap_service.create_mindmap(db, mindmap, current_user.id)

@router.get("/mindmaps/", response_model=List[MindMapResponse])
async def list_mindmaps(
    current_user = Depends(get_current_user),
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 10
):
    """List all mind maps for the current user"""
    return mindmap_service.get_user_mindmaps(db, current_user.id, skip, limit)

@router.get("/mindmaps/{mindmap_id}", response_model=MindMapResponse)
async def get_mindmap(
    mindmap_id: int,
    current_user = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get a specific mind map"""
    mindmap = mindmap_service.get_mindmap(db, mindmap_id)
    if not mindmap or mindmap.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Mind map not found")
    return mindmap

@router.put("/mindmaps/{mindmap_id}", response_model=MindMapResponse)
async def update_mindmap(
    mindmap_id: int,
    mindmap_update: MindMapUpdate,
    current_user = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Update a mind map"""
    mindmap = mindmap_service.get_mindmap(db, mindmap_id)
    if not mindmap or mindmap.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Mind map not found")
    return mindmap_service.update_mindmap(db, mindmap, mindmap_update)

@router.delete("/mindmaps/{mindmap_id}")
async def delete_mindmap(
    mindmap_id: int,
    current_user = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Delete a mind map"""
    mindmap = mindmap_service.get_mindmap(db, mindmap_id)
    if not mindmap or mindmap.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Mind map not found")
    mindmap_service.delete_mindmap(db, mindmap_id)
    return {"message": "Mind map deleted successfully"}

@router.post("/mindmaps/{mindmap_id}/nodes/", response_model=NodeResponse)
async def create_node(
    mindmap_id: int,
    node: NodeCreate,
    current_user = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Create a new node in a mind map"""
    mindmap = mindmap_service.get_mindmap(db, mindmap_id)
    if not mindmap or mindmap.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Mind map not found")
    return mindmap_service.create_node(db, mindmap_id, node)

@router.put("/mindmaps/{mindmap_id}/nodes/{node_id}", response_model=NodeResponse)
async def update_node(
    mindmap_id: int,
    node_id: int,
    node_update: NodeUpdate,
    current_user = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Update a node in a mind map"""
    mindmap = mindmap_service.get_mindmap(db, mindmap_id)
    if not mindmap or mindmap.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Mind map not found")
    return mindmap_service.update_node(db, node_id, node_update)

@router.delete("/mindmaps/{mindmap_id}/nodes/{node_id}")
async def delete_node(
    mindmap_id: int,
    node_id: int,
    current_user = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Delete a node from a mind map"""
    mindmap = mindmap_service.get_mindmap(db, mindmap_id)
    if not mindmap or mindmap.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Mind map not found")
    mindmap_service.delete_node(db, node_id)
    return {"message": "Node deleted successfully"}

@router.post("/mindmaps/{mindmap_id}/ai/analyze")
async def analyze_mindmap(
    mindmap_id: int,
    current_user = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Analyze mind map structure using AI"""
    mindmap = mindmap_service.get_mindmap(db, mindmap_id)
    if not mindmap or mindmap.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Mind map not found")
    return await ai_service.analyze_structure(mindmap)

@router.post("/mindmaps/{mindmap_id}/ai/suggest")
async def get_suggestions(
    mindmap_id: int,
    node_id: int,
    current_user = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get AI suggestions for a specific node"""
    mindmap = mindmap_service.get_mindmap(db, mindmap_id)
    if not mindmap or mindmap.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Mind map not found")
    return await ai_service.generate_suggestions(mindmap, node_id)

@router.websocket("/ws/mindmap/{mindmap_id}")
async def websocket_endpoint(
    websocket: WebSocket,
    mindmap_id: int,
    token: str,
    db: Session = Depends(get_db)
):
    """WebSocket endpoint for real-time collaboration"""
    await websocket.accept()
    try:
        # Verify token and get user
        current_user = get_current_user(token)
        mindmap = mindmap_service.get_mindmap(db, mindmap_id)
        if not mindmap or mindmap.user_id != current_user.id:
            await websocket.close(code=4004)
            return

        # Handle real-time updates
        while True:
            data = await websocket.receive_json()
            # Process the update
            response = await mindmap_service.process_realtime_update(db, mindmap_id, data)
            # Broadcast to all connected clients
            await websocket.send_json(response)
    except Exception as e:
        await websocket.close(code=4000)
    finally:
        await websocket.close() 