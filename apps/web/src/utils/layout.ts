import { MindMapNode, MindMapEdge } from '@/types/mindmap';

export const calculateNodePosition = (
  parentNode: MindMapNode,
  childIndex: number,
  totalChildren: number
) => {
  const HORIZONTAL_SPACING = 200;
  const VERTICAL_SPACING = 100;
  
  const angle = (childIndex / totalChildren) * Math.PI - Math.PI / 2;
  const radius = HORIZONTAL_SPACING;
  
  return {
    x: parentNode.position.x + Math.cos(angle) * radius,
    y: parentNode.position.y + Math.sin(angle) * radius + VERTICAL_SPACING,
  };
};

export const organizeLayout = (nodes: MindMapNode[], edges: MindMapEdge[]) => {
  const nodeMap = new Map(nodes.map(node => [node.id, node]));
  const childrenMap = new Map<string, string[]>();
  
  edges.forEach(edge => {
    const children = childrenMap.get(edge.source) || [];
    children.push(edge.target);
    childrenMap.set(edge.source, children);
  });
  
  const updatePositions = (nodeId: string, level: number = 0) => {
    const children = childrenMap.get(nodeId) || [];
    const parentNode = nodeMap.get(nodeId);
    
    if (!parentNode) return;
    
    children.forEach((childId, index) => {
      const childNode = nodeMap.get(childId);
      if (childNode) {
        const position = calculateNodePosition(parentNode, index, children.length);
        childNode.position = position;
        updatePositions(childId, level + 1);
      }
    });
  };
  
  const rootNode = nodes.find(node => node.id === '1');
  if (rootNode) {
    updatePositions(rootNode.id);
  }
  
  return nodes.map(node => ({
    ...node,
    position: nodeMap.get(node.id)?.position || node.position,
  }));
}; 