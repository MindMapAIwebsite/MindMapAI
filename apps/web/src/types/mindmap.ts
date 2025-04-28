import { Node, Edge } from 'reactflow';

export interface MindMapNode extends Node {
  data: {
    label: string;
    description?: string;
  };
}

export interface MindMapEdge extends Edge {
  data?: {
    type?: string;
  };
}

export interface MindMapData {
  nodes: MindMapNode[];
  edges: MindMapEdge[];
} 