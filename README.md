# MindMap AI - Intelligent Mind Mapping Platform

<div align="center">
  <img src="./assets/images/logo.png" alt="MindMap AI Logo" width="800" style="border-radius: 50%;">
  
  [![Website](https://img.shields.io/badge/Website-MindMapAI.website-blue)](https://www.MindMapAI.website/)
  [![Twitter](https://img.shields.io/badge/Twitter-MindMapAI__-blue)](https://x.com/MindMapAI_)
  [![GitHub](https://img.shields.io/badge/GitHub-MindMapAIwebsite-blue)](https://github.com/MindMapAIwebsite/MindMapAI)
</div>

## 🔑 Overview

MindMap AI revolutionizes the way we create and manage mind maps by leveraging artificial intelligence. Our platform transforms complex ideas into clear, intuitive mind maps through intelligent content organization and real-time AI collaboration.

### Key Features

- **Intelligent Content Organization**: Transform text and documents into structured mind maps
- **AI Copilot**: Real-time brainstorming and creative enhancement
- **Interactive Editing**: Intuitive drag-and-drop interface
- **Smart Layout**: Automatic node positioning and organization
- **Real-time Collaboration**: Multi-user editing and cloud synchronization
- **Export Options**: Multiple format support for sharing and presentation

## 🏗️ System Architecture

MindMap AI employs a modern, scalable architecture designed for performance and AI integration.

### High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                        Client Applications                          │
│                                                                     │
│   ┌─────────────────┐   ┌─────────────────┐   ┌─────────────────┐   │
│   │   Web App       │   │   Mobile App    │   │   Desktop App   │   │
│   │   (React/TS)    │   │   (React Native)│   │   (Electron)    │   │
│   └─────────────────┘   └─────────────────┘   └─────────────────┘   │
└────────────────────────────────┬────────────────────────────────────┘
                                 │
                                 ▼
┌─────────────────────────────────────────────────────────────────────┐
│                           API Gateway                               │
│                                                                     │
│   ┌─────────────────┐   ┌─────────────────┐   ┌─────────────────┐   │
│   │  Authentication │   │   API Routing   │   │   Rate Limiting │   │
│   │  & Authorization│   │   & Validation  │   │   & Security    │   │
│   └─────────────────┘   └─────────────────┘   └─────────────────┘   │
└────────────────────────────────┬────────────────────────────────────┘
                                 │
                                 ▼
┌─────────────────────────────────────────────────────────────────────┐
│                        Backend Services                             │
│                                                                     │
│ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐    │
│ │ Mind Map    │ │ AI Content  │ │ User        │ │ Collaboration│    │
│ │ Service     │ │ Processing  │ │ Service     │ │ Service      │    │
│ └─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘    │
│                                                                     │
│ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐    │
│ │ AI Copilot  │ │ Export      │ │ Analytics   │ │ Storage     │    │
│ │ Service     │ │ Service     │ │ Service     │ │ Service     │    │
│ └─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘    │
└────────────────────────────────┬────────────────────────────────────┘
                                 │
                                 ▼
┌─────────────────────────────────────────────────────────────────────┐
│                        AI Processing Layer                          │
│                                                                     │
│   ┌─────────────────┐   ┌─────────────────┐   ┌─────────────────┐   │
│   │  NLP Engine     │   │  Content        │   │  Layout         │   │
│   │  & LLM Models   │   │  Analysis       │   │  Optimization   │   │
│   └─────────────────┘   └─────────────────┘   └─────────────────┘   │
└────────────────────────────────┬────────────────────────────────────┘
                                 │
                                 ▼
┌─────────────────────────────────────────────────────────────────────┐
│                         Data Layer                                  │
│                                                                     │
│   ┌─────────────────┐   ┌─────────────────┐   ┌─────────────────┐   │
│   │   PostgreSQL    │   │     Redis       │   │    S3 Storage   │   │
│   │   Database      │   │     Cache       │   │    & CDN        │   │
│   └─────────────────┘   └─────────────────┘   └─────────────────┘   │
└─────────────────────────────────────────────────────────────────────┘
```

## 💻 Technical Stack

### Frontend
- **Framework**: React with TypeScript
- **State Management**: React Hooks
- **UI Components**: Custom components with Tailwind CSS
- **Visualization**: React Flow for mind map rendering
- **API Integration**: Axios, React Query

### Backend
- **Framework**: Next.js API Routes
- **Authentication**: JWT with OAuth2
- **Database**: PostgreSQL with Prisma
- **Cache**: Redis
- **Storage**: AWS S3

### AI Infrastructure
- **NLP**: OpenAI GPT-4
- **Layout Engine**: Custom algorithms
- **Content Analysis**: Machine Learning models

## 🚀 Getting Started

### Prerequisites
- Node.js (v16+)
- npm or yarn
- PostgreSQL (v14+)
- Redis

### Installation

```bash
# Clone the repository
git clone https://github.com/MindMapAIwebsite/MindMapAI.git
cd MindMapAI

# Install dependencies
cd apps/web
npm install

# Set up environment variables
cp .env.example .env
# Edit .env with your configuration

# Start development server
npm run dev
```

## 📊 Core Features

### Content Processing
- Text to Mind Map conversion
- Document analysis
- Hierarchical structure detection
- Smart content organization

### AI Copilot
- Real-time suggestions
- Knowledge gap detection
- Creative expansion
- Context-aware recommendations

### Collaboration
- Real-time multi-user editing
- Version control
- Share and export options
- Team workspaces

## 🔒 Security

- End-to-end encryption for sensitive data
- OAuth2 authentication
- Rate limiting
- GDPR compliance
- Regular security audits

## 📖 Documentation

- [User Guide](docs/user_guide.md)
- [API Reference](docs/api_reference.md)
- [Development Guide](docs/development.md)
- [AI Features](docs/ai_features.md)

## 🤝 Contributing

We welcome contributions! Please read our [Contributing Guidelines](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

### Development Workflow

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Contact

- Website: [mindmapai.website](https://www.mindmapai.website)
- Twitter: [@MindMapAI_](https://x.com/MindMapAI_)
- GitHub: [MindMapAIwebsite](https://github.com/MindMapAIwebsite/MindMapAI)

Built with ❤️ by the MindMap AI Team 