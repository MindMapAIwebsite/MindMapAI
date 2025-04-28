import { useCallback, useState } from 'react';
import ReactFlow, {
  Node,
  Edge,
  Controls,
  Background,
  useNodesState,
  useEdgesState,
  addEdge,
  Connection,
  NodeChange,
  EdgeChange,
  ConnectionMode,
} from 'reactflow';
import 'reactflow/dist/style.css';

const initialNodes: Node[] = [
  {
    id: '1',
    type: 'input',
    data: { label: 'Central Topic' },
    position: { x: 250, y: 100 },
  },
];

const initialEdges: Edge[] = [];

export interface MindMapProps {
  className?: string;
}

export const MindMap: React.FC<MindMapProps> = ({ className }) => {
  const [nodes, setNodes, onNodesChange] = useNodesState(initialNodes);
  const [edges, setEdges, onEdgesChange] = useEdgesState(initialEdges);

  const onConnect = useCallback(
    (connection: Connection) => {
      setEdges((eds) => addEdge(connection, eds));
    },
    [setEdges]
  );

  const handleAddChild = useCallback(() => {
    const newNodeId = (nodes.length + 1).toString();
    const newNode: Node = {
      id: newNodeId,
      data: { label: `Topic ${newNodeId}` },
      position: {
        x: Math.random() * 500,
        y: Math.random() * 300,
      },
    };

    setNodes((nds) => [...nds, newNode]);
    setEdges((eds) => [
      ...eds,
      {
        id: `e${nodes[0].id}-${newNodeId}`,
        source: nodes[0].id,
        target: newNodeId,
      },
    ]);
  }, [nodes, setNodes, setEdges]);

  return (
    <div className={`h-[600px] ${className}`}>
      <div className="absolute top-4 left-4 z-10">
        <button
          onClick={handleAddChild}
          className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
        >
          Add Topic
        </button>
      </div>
      <ReactFlow
        nodes={nodes}
        edges={edges}
        onNodesChange={onNodesChange}
        onEdgesChange={onEdgesChange}
        onConnect={onConnect}
        connectionMode={ConnectionMode.Loose}
        fitView
      >
        <Background />
        <Controls />
      </ReactFlow>
    </div>
  );
};

export default MindMap; 