import './App.css'

const GITHUB_URL = 'https://github.com/andrey-tsykunov/license-to-play'

const frameworks = [
  {
    id: 'agno',
    name: 'Agno',
    icon: '⚡',
    color: '#6366f1',
    description: 'Most fully-featured implementation with multi-agent teams, AgentOS orchestration, REST API, and A2A (Agent-to-Agent) interface.',
    agents: ['fee_agent', 'complain_agent', 'math_agent', 'support_agent', 'research_agent', 'agno_docs_agent'],
    features: ['FastAPI REST server', 'A2A interface', 'Skills system', 'SQLite persistence'],
    badge: 'Featured',
  },
  {
    id: 'langgraph',
    name: 'LangGraph',
    icon: '🔗',
    color: '#10b981',
    description: "StateGraph-based orchestration using LangChain's LangGraph framework with configurable agent graphs.",
    agents: ['math_agent', 'research_agent'],
    features: ['StateGraph orchestration', 'langgraph.json config', 'LangSmith tracing'],
    badge: null,
  },
  {
    id: 'google-adk',
    name: 'Google ADK',
    icon: '🌐',
    color: '#f59e0b',
    description: "Google's Agent Development Kit with Gemini models, supporting root and time agents.",
    agents: ['root_agent', 'time_agent'],
    features: ['Gemini models', 'ADK web UI', 'Native Google integration'],
    badge: null,
  },
  {
    id: 'claude',
    name: 'Claude SDK',
    icon: '🤖',
    color: '#ec4899',
    description: "Anthropic's Claude Agent SDK with async streaming and multi-turn conversation support.",
    agents: ['basic_agent', 'streaming_input_agent'],
    features: ['Async streaming', 'Native Claude integration', 'Multi-turn conversations'],
    badge: null,
  },
  {
    id: 'openai',
    name: 'OpenAI',
    icon: '✦',
    color: '#3b82f6',
    description: 'OpenAI agents SDK with multi-language support and agent handoff capabilities.',
    agents: ['multi_language_agent'],
    features: ['Agent handoffs', 'Multi-language support', 'Session-based'],
    badge: null,
  },
  {
    id: 'microsoft',
    name: 'Microsoft',
    icon: '🪟',
    color: '#8b5cf6',
    description: 'Microsoft agent framework implementation with session management and basic agent capabilities.',
    agents: ['basic_agent'],
    features: ['Session management', 'Azure compatible', 'Basic agent pattern'],
    badge: null,
  },
  {
    id: 'pydantic-ai',
    name: 'Pydantic AI',
    icon: '🏗️',
    color: '#e11d48',
    description: 'Type-safe agent framework built on Pydantic. Unique feature: structured typed outputs — the LLM returns validated Pydantic models instead of raw text, with full IDE autocompletion.',
    agents: ['research_agent'],
    features: ['Structured typed outputs', 'Runtime validation', 'Multi-provider support', 'JSON serialisation'],
    badge: 'Structured Output',
  },
]

const providers = [
  { name: 'Anthropic Claude', icon: '🤖', color: '#ec4899' },
  { name: 'OpenAI GPT', icon: '✦', color: '#3b82f6' },
  { name: 'Google Gemini', icon: '🌐', color: '#f59e0b' },
  { name: 'Ollama (local)', icon: '🦙', color: '#10b981' },
]

const tools = [
  { name: 'Tavily', desc: 'Web search' },
  { name: 'Firecrawl', desc: 'Web scraping' },
  { name: 'Perplexity', desc: 'AI research' },
  { name: 'LangSmith', desc: 'Agent monitoring' },
  { name: 'Arize Phoenix', desc: 'Observability' },
  { name: 'OpenTelemetry', desc: 'Distributed tracing' },
]

function Badge({ text, color }) {
  return (
    <span className="badge" style={{ background: color + '22', color, border: `1px solid ${color}44` }}>
      {text}
    </span>
  )
}

function GitHubIcon() {
  return (
    <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
      <path d="M12 0C5.374 0 0 5.373 0 12c0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23A11.509 11.509 0 0 1 12 5.803c1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576C20.566 21.797 24 17.3 24 12c0-6.627-5.373-12-12-12z"/>
    </svg>
  )
}

function FrameworkCard({ fw }) {
  return (
    <div className="card framework-card">
      <div className="card-header">
        <div className="fw-icon" style={{ background: fw.color + '22', color: fw.color }}>
          {fw.icon}
        </div>
        <div className="fw-title-row">
          <h3 className="fw-name">{fw.name}</h3>
          {fw.badge && <Badge text={fw.badge} color={fw.color} />}
        </div>
      </div>
      <p className="fw-description">{fw.description}</p>
      <div className="fw-section">
        <span className="fw-section-label">Agents</span>
        <div className="tags">
          {fw.agents.map(a => (
            <span key={a} className="tag tag-agent">{a}</span>
          ))}
        </div>
      </div>
      <div className="fw-section">
        <span className="fw-section-label">Features</span>
        <ul className="feature-list">
          {fw.features.map(f => (
            <li key={f}><span className="check" style={{ color: fw.color }}>✓</span> {f}</li>
          ))}
        </ul>
      </div>
    </div>
  )
}

function App() {
  return (
    <div className="app">
      {/* Nav */}
      <nav className="nav">
        <div className="nav-inner container">
          <span className="nav-logo">🎮 license-to-play</span>
          <a href={GITHUB_URL} target="_blank" rel="noopener noreferrer" className="nav-gh">
            <GitHubIcon /> GitHub
          </a>
        </div>
      </nav>

      {/* Hero */}
      <header className="hero">
        <div className="hero-glow hero-glow-1" />
        <div className="hero-glow hero-glow-2" />
        <div className="container hero-content">
          <div className="hero-eyebrow">
            <span className="eyebrow-dot" />
            Agentic AI Experimentation
          </div>
          <h1 className="hero-title">
            License to <span className="gradient-text">Play</span>
          </h1>
          <p className="hero-subtitle">
            A multi-framework playground comparing agentic AI implementations across
            Agno, LangGraph, Google ADK, Claude SDK, and OpenAI — using the same core
            agents as a cross-framework benchmark.
          </p>
          <div className="hero-actions">
            <a href={GITHUB_URL} target="_blank" rel="noopener noreferrer" className="btn btn-primary">
              <GitHubIcon /> View on GitHub
            </a>
            <a href={`${GITHUB_URL}#readme`} target="_blank" rel="noopener noreferrer" className="btn btn-secondary">
              Read the Docs
            </a>
          </div>
          <div className="hero-stats">
            <div className="stat">
              <span className="stat-value">7</span>
              <span className="stat-label">Frameworks</span>
            </div>
            <div className="stat-divider" />
            <div className="stat">
              <span className="stat-value">10+</span>
              <span className="stat-label">Agents</span>
            </div>
            <div className="stat-divider" />
            <div className="stat">
              <span className="stat-value">4</span>
              <span className="stat-label">LLM Providers</span>
            </div>
          </div>
        </div>
      </header>

      {/* What is it */}
      <section className="section section-alt">
        <div className="container">
          <div className="section-header">
            <h2 className="section-title">What is License to Play?</h2>
            <p className="section-subtitle">
              A hands-on comparison of agentic AI frameworks, all implementing the same
              core agents so you can evaluate each framework's strengths, patterns, and
              trade-offs side by side.
            </p>
          </div>
          <div className="feature-grid">
            <div className="card feature-card">
              <div className="feature-icon">🔬</div>
              <h3>Cross-Framework Comparison</h3>
              <p>Same agents (math, research, support) implemented across 6 frameworks — a true apples-to-apples benchmark.</p>
            </div>
            <div className="card feature-card">
              <div className="feature-icon">🔌</div>
              <h3>Multi-Provider Support</h3>
              <p>Swap LLM providers at runtime via <code>DEFAULT_AGENT_MODEL</code> — Claude, GPT, Gemini, or local Ollama.</p>
            </div>
            <div className="card feature-card">
              <div className="feature-icon">📡</div>
              <h3>REST &amp; A2A APIs</h3>
              <p>Agents expose REST endpoints and Agent-to-Agent (A2A) interfaces for composable, programmable interaction.</p>
            </div>
            <div className="card feature-card">
              <div className="feature-icon">🔭</div>
              <h3>Built-in Observability</h3>
              <p>Arize Phoenix + OpenTelemetry tracing across all frameworks. Spin up Phoenix and traces flow automatically.</p>
            </div>
          </div>
        </div>
      </section>

      {/* Frameworks */}
      <section className="section">
        <div className="container">
          <div className="section-header">
            <h2 className="section-title">Agent Frameworks</h2>
            <p className="section-subtitle">
              Each framework lives in its own <code>src/&lt;framework&gt;_agent/</code> directory
              with a consistent internal structure.
            </p>
          </div>
          <div className="frameworks-grid">
            {frameworks.map(fw => <FrameworkCard key={fw.id} fw={fw} />)}
          </div>
        </div>
      </section>

      {/* LLM Providers */}
      <section className="section section-alt">
        <div className="container">
          <div className="section-header">
            <h2 className="section-title">LLM Providers</h2>
            <p className="section-subtitle">Configure once, swap anytime via environment variables.</p>
          </div>
          <div className="providers-grid">
            {providers.map(p => (
              <div key={p.name} className="card provider-card">
                <span className="provider-icon" style={{ color: p.color }}>{p.icon}</span>
                <span className="provider-name">{p.name}</span>
              </div>
            ))}
          </div>
          <div className="code-block">
            <div className="code-block-header">
              <span>Environment Configuration</span>
              <span className="code-lang">bash</span>
            </div>
            <pre><code>{`# Default model (any provider)
DEFAULT_AGENT_MODEL=claude-haiku-4-5-20251001

# API Keys
ANTHROPIC_API_KEY=...
OPENAI_API_KEY=...
GOOGLE_API_KEY=...

# Tool integrations
TAVILY_API_KEY=...
FIRECRAWL_API_KEY=...`}</code></pre>
          </div>
        </div>
      </section>

      {/* Tools */}
      <section className="section">
        <div className="container">
          <div className="section-header">
            <h2 className="section-title">Tools &amp; Integrations</h2>
            <p className="section-subtitle">External APIs and observability platforms wired in out of the box.</p>
          </div>
          <div className="tools-grid">
            {tools.map(t => (
              <div key={t.name} className="card tool-card">
                <div className="tool-name">{t.name}</div>
                <div className="tool-desc">{t.desc}</div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Quick Start */}
      <section className="section section-alt">
        <div className="container">
          <div className="section-header">
            <h2 className="section-title">Quick Start</h2>
            <p className="section-subtitle">Up and running in minutes.</p>
          </div>
          <div className="quickstart-grid">
            <div className="code-block">
              <div className="code-block-header">
                <span>Install &amp; Run (Agno)</span>
                <span className="code-lang">bash</span>
              </div>
              <pre><code>{`# Install dependencies
uv sync --all-groups

# Copy and fill in env vars
cp .env.example .env

# Start Agno REST server
fastapi dev --port 7777 \\
  src/agno_agent/server2.py

# Observability (optional)
uv run python -m phoenix.server.main serve`}</code></pre>
            </div>
            <div className="code-block">
              <div className="code-block-header">
                <span>Other Frameworks</span>
                <span className="code-lang">bash</span>
              </div>
              <pre><code>{`# Run tests
pytest -s src

# LangGraph
langgraph dev       # Port 2024

# Google ADK
adk web src

# Agno AgentOS UI
fastapi dev src/agno_agent/server1.py`}</code></pre>
            </div>
          </div>
        </div>
      </section>

      {/* CTA */}
      <section className="section cta-section">
        <div className="container cta-content">
          <h2 className="cta-title">Ready to experiment?</h2>
          <p className="cta-subtitle">
            Clone the repo, pick your framework, and start comparing agentic AI patterns.
          </p>
          <a href={GITHUB_URL} target="_blank" rel="noopener noreferrer" className="btn btn-primary btn-lg">
            <GitHubIcon /> Star on GitHub
          </a>
        </div>
      </section>

      <footer className="footer">
        <div className="container footer-content">
          <span>License to Play</span>
          <span className="footer-sep">·</span>
          <a href={GITHUB_URL} target="_blank" rel="noopener noreferrer">GitHub</a>
          <span className="footer-sep">·</span>
          <span>Built with React + Vite</span>
        </div>
      </footer>
    </div>
  )
}

export default App
