import { MindMap } from '@/components/MindMap/MindMap';

export default function Home() {
  return (
    <main className="min-h-screen p-8">
      <h1 className="text-3xl font-bold mb-8">Mind Map Creator</h1>
      <MindMap className="w-full border rounded-lg shadow-lg" />
    </main>
  );
} 