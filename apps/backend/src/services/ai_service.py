import openai
from typing import List, Dict, Any
import numpy as np
from transformers import pipeline
import cv2
import torch
from ..models.mindmap import MindMap, Node
from ..core.config import settings

class AIService:
    def __init__(self):
        self.openai_client = openai.OpenAI(api_key=settings.OPENAI_API_KEY)
        self.text_analyzer = pipeline("text-classification", model="distilbert-base-uncased")
        self.image_analyzer = pipeline("image-classification", model="google/vit-base-patch16-224")
        
    async def analyze_structure(self, mindmap: MindMap) -> Dict[str, Any]:
        """Analyze the mind map structure and provide insights"""
        try:
            # Extract mind map structure
            nodes = self._extract_node_structure(mindmap)
            
            # Analyze using OpenAI
            analysis = await self._analyze_with_openai(nodes)
            
            # Process and enhance the analysis
            enhanced_analysis = self._enhance_analysis(analysis)
            
            return {
                "analysis": enhanced_analysis,
                "suggestions": self._generate_structure_suggestions(enhanced_analysis),
                "metrics": self._calculate_structure_metrics(nodes)
            }
        except Exception as e:
            print(f"Error in analyze_structure: {str(e)}")
            return {"error": "Failed to analyze mind map structure"}

    async def generate_suggestions(self, mindmap: MindMap, node_id: int) -> Dict[str, Any]:
        """Generate AI suggestions for a specific node"""
        try:
            # Get node context
            node_context = self._get_node_context(mindmap, node_id)
            
            # Generate suggestions using OpenAI
            suggestions = await self._generate_node_suggestions(node_context)
            
            return {
                "suggestions": suggestions,
                "relevance_score": self._calculate_relevance_score(suggestions, node_context),
                "context": self._extract_relevant_context(node_context)
            }
        except Exception as e:
            print(f"Error in generate_suggestions: {str(e)}")
            return {"error": "Failed to generate suggestions"}

    async def process_content(self, content: str, content_type: str) -> Dict[str, Any]:
        """Process different types of content and extract mind map structure"""
        try:
            if content_type == "text":
                return await self._process_text_content(content)
            elif content_type == "pdf":
                return await self._process_pdf_content(content)
            elif content_type == "image":
                return await self._process_image_content(content)
            elif content_type == "audio":
                return await self._process_audio_content(content)
            else:
                raise ValueError(f"Unsupported content type: {content_type}")
        except Exception as e:
            print(f"Error in process_content: {str(e)}")
            return {"error": f"Failed to process {content_type} content"}

    async def _analyze_with_openai(self, nodes: List[Dict]) -> Dict[str, Any]:
        """Analyze mind map structure using OpenAI API"""
        try:
            response = await self.openai_client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are an AI expert in analyzing mind maps and providing insights."},
                    {"role": "user", "content": f"Analyze this mind map structure and provide insights: {str(nodes)}"}
                ],
                temperature=0.7,
                max_tokens=500
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error in _analyze_with_openai: {str(e)}")
            return {"error": "Failed to analyze with OpenAI"}

    async def _generate_node_suggestions(self, context: Dict) -> List[Dict]:
        """Generate suggestions for a node using OpenAI API"""
        try:
            response = await self.openai_client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are an AI expert in mind mapping and brainstorming."},
                    {"role": "user", "content": f"Generate relevant suggestions for this mind map node: {str(context)}"}
                ],
                temperature=0.8,
                max_tokens=300
            )
            return self._parse_suggestions(response.choices[0].message.content)
        except Exception as e:
            print(f"Error in _generate_node_suggestions: {str(e)}")
            return []

    def _extract_node_structure(self, mindmap: MindMap) -> List[Dict]:
        """Extract the structure of nodes from the mind map"""
        nodes = []
        for node in mindmap.nodes:
            nodes.append({
                "id": node.id,
                "text": node.text,
                "connections": [conn.target_id for conn in node.connections],
                "depth": self._calculate_node_depth(node),
                "children_count": len(node.connections)
            })
        return nodes

    def _calculate_node_depth(self, node: Node, visited=None) -> int:
        """Calculate the depth of a node in the mind map"""
        if visited is None:
            visited = set()
        if not node.parent_id or node.id in visited:
            return 0
        visited.add(node.id)
        return 1 + self._calculate_node_depth(node.parent, visited)

    def _enhance_analysis(self, analysis: Dict) -> Dict:
        """Enhance the analysis with additional insights"""
        return {
            "structure_quality": self._analyze_structure_quality(analysis),
            "balance_score": self._calculate_balance_score(analysis),
            "complexity_metrics": self._calculate_complexity_metrics(analysis),
            "improvement_suggestions": self._generate_improvement_suggestions(analysis)
        }

    def _calculate_structure_metrics(self, nodes: List[Dict]) -> Dict:
        """Calculate various metrics about the mind map structure"""
        return {
            "total_nodes": len(nodes),
            "max_depth": max(node["depth"] for node in nodes),
            "avg_connections": sum(len(node["connections"]) for node in nodes) / len(nodes),
            "complexity_score": self._calculate_complexity_score(nodes)
        }

    def _calculate_complexity_score(self, nodes: List[Dict]) -> float:
        """Calculate a complexity score for the mind map"""
        total_connections = sum(len(node["connections"]) for node in nodes)
        max_depth = max(node["depth"] for node in nodes)
        return (total_connections * max_depth) / len(nodes)

    def _calculate_relevance_score(self, suggestions: List[Dict], context: Dict) -> float:
        """Calculate relevance score for suggestions"""
        # Implement relevance scoring logic
        return 0.85  # Placeholder

    def _extract_relevant_context(self, context: Dict) -> Dict:
        """Extract relevant context for suggestions"""
        return {
            "topic": context.get("topic"),
            "related_concepts": context.get("related_concepts", [])[:5],
            "hierarchy_level": context.get("hierarchy_level")
        }

    def _parse_suggestions(self, content: str) -> List[Dict]:
        """Parse and structure the suggestions from OpenAI response"""
        # Implement suggestion parsing logic
        return []  # Placeholder 