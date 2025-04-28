# MindMap AI

![MindMap AI Logo](assets/logo.png)

A powerful and intuitive mind mapping tool powered by AI.

## Features

- Interactive mind map creation and editing
- Real-time collaboration
- AI-powered topic suggestions
- Customizable node styles and layouts
- Export to various formats
- Keyboard shortcuts for efficient navigation

## Tech Stack

- **Frontend**: Next.js, React, TypeScript
- **State Management**: React Hooks
- **Visualization**: React Flow
- **Styling**: Tailwind CSS
- **AI Integration**: OpenAI API

## Project Structure

```
apps/web/
├── src/
│   ├── components/    # React components
│   │   └── MindMap/  # Mind map related components
│   ├── hooks/        # Custom React hooks
│   ├── pages/        # Next.js pages
│   ├── styles/       # Global styles
│   ├── types/        # TypeScript type definitions
│   └── utils/        # Utility functions
├── public/           # Static assets
└── tests/           # Test files
```

## Architecture

### Data Flow
```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   User      │    │  React      │    │  Mind Map   │
│ Interaction │───>│   State     │───>│   Render    │
└─────────────┘    └─────────────┘    └─────────────┘
       │                  ▲                  │
       │                  │                  │
       └──────────────────┴──────────────────┘
```

### Component Architecture
```
┌─────────────────┐
│    MindMap      │
└────────┬────────┘
         │
    ┌────┴────┐
    │         │
┌───▼───┐ ┌───▼───┐
│ Nodes │ │ Edges │
└───────┘ └───────┘
```

## Getting Started

1. Clone the repository:
```bash
git clone https://github.com/MindMapAIwebsite/MindMapAI.git
```

2. Install dependencies:
```bash
cd MindMapAI/apps/web
npm install
```

3. Start the development server:
```bash
npm run dev
```

4. Open [http://localhost:3000](http://localhost:3000) in your browser.

## Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

## Links

- Website: [https://www.MindMapAI.website/](https://www.MindMapAI.website/)
- Twitter: [https://x.com/MindMapAI_](https://x.com/MindMapAI_)
- GitHub: [https://github.com/MindMapAIwebsite/MindMapAI](https://github.com/MindMapAIwebsite/MindMapAI)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 