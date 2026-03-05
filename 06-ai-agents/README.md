# Stage 6 — AI Agents

## 🎯 Learning Objectives

By the end of this stage you will:
- Understand core agent architectures (ReAct, Plan-and-Execute, Function Calling)
- Build tool-using agents that interact with external APIs and services
- Implement memory systems (short-term, long-term, episodic) for persistent agents
- Design and orchestrate multi-agent systems for complex workflows
- Work with agent frameworks (LangGraph, CrewAI, AutoGen)
- Apply prompt engineering techniques specifically for agentic systems
- Evaluate, test, and debug AI agents systematically
- Deploy production-ready agents with safety guardrails

## ⏱️ Estimated Time: 3 weeks

---

## 📐 Key Concepts

### 1. Agent Architectures

An AI agent is a system that uses an LLM as its reasoning engine to decide what actions to take, execute those actions, observe the results, and iterate until a goal is achieved.

```
User Goal → LLM (Reasoning) → Action Selection → Tool Execution → Observation → ... → Final Answer
```

| Architecture | How It Works | Best For |
|---|---|---|
| ReAct | Interleave Reasoning + Acting in a loop | General-purpose tool use |
| Plan-and-Execute | Create full plan first, then execute steps | Complex multi-step tasks |
| Function Calling | LLM outputs structured tool calls natively | API integration, structured output |
| Reflexion | Agent reflects on failures and retries | Self-correcting workflows |
| LATS (Language Agent Tree Search) | Tree search over possible action sequences | High-stakes decision making |
| Tool-Use Only | Single tool call, no reasoning loop | Simple retrieval or API calls |

#### ReAct Agent Loop

```
Thought:  I need to find the latest revenue figures for Company X.
Action:   web_search("Company X Q4 2024 revenue")
Observation: Company X reported $12.3B in Q4 2024 revenue...
Thought:  Now I need to compare this to Q3.
Action:   web_search("Company X Q3 2024 revenue")
Observation: Company X reported $11.1B in Q3 2024...
Thought:  Revenue grew by ~10.8% QoQ. I can now answer.
Final Answer: Company X's Q4 2024 revenue was $12.3B, up 10.8% from Q3's $11.1B.
```

#### Plan-and-Execute Architecture

```
User Query
    ↓
┌─────────────┐
│   Planner   │ → Generates ordered list of subtasks
└─────────────┘
    ↓
┌─────────────┐
│  Executor   │ → Executes each subtask using tools
└─────────────┘
    ↓
┌─────────────┐
│  Re-planner │ → Adjusts remaining plan based on results
└─────────────┘
    ↓
Final Output
```

### 2. Tool Use and Function Calling

Tools give agents the ability to interact with the outside world — search the web, run code, query databases, call APIs, and more.

| Tool Category | Examples | Use Case |
|---|---|---|
| Search | Tavily, SerpAPI, Brave Search | Web search and information retrieval |
| Code Execution | Python REPL, E2B sandbox | Running code, data analysis |
| APIs | REST calls, GraphQL | External service integration |
| Databases | SQL queries, vector search | Data retrieval and storage |
| File System | Read/write files | Document processing |
| Browser | Playwright, Selenium | Web scraping, form filling |
| Communication | Email, Slack, webhooks | Notifications and collaboration |

**OpenAI Function Calling Example:**

```python
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get the current weather for a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "City and state, e.g. San Francisco, CA"
                    },
                    "unit": {
                        "type": "string",
                        "enum": ["celsius", "fahrenheit"]
                    }
                },
                "required": ["location"]
            }
        }
    }
]

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "What's the weather in Paris?"}],
    tools=tools,
    tool_choice="auto"
)
```

### 3. Memory Systems

Agents need memory to maintain context across interactions and learn from past experiences.

| Memory Type | Duration | Implementation | Example |
|---|---|---|---|
| Short-term (Working) | Single session | Conversation buffer, sliding window | Current chat messages |
| Long-term (Semantic) | Persistent | Vector database storage | Past conversations, facts |
| Episodic | Persistent | Structured experience logs | "Last time user asked X, they wanted Y" |
| Procedural | Persistent | Tool/skill library | Learned action sequences |
| Entity | Persistent | Knowledge graph / key-value store | User preferences, entity relationships |

```
Agent Memory Architecture
┌───────────────────────────────────────────┐
│              Agent Core (LLM)             │
├───────────────┬───────────┬───────────────┤
│  Short-term   │  Episodic │   Long-term   │
│  (Buffer)     │  (Logs)   │  (Vector DB)  │
│               │           │               │
│ Recent msgs   │ Past task │ Knowledge     │
│ Current ctx   │ outcomes  │ base          │
│ Scratch pad   │ Feedback  │ User profile  │
└───────────────┴───────────┴───────────────┘
```

### 4. Multi-Agent Systems and Collaboration

Multi-agent systems decompose complex problems across specialized agents that communicate and collaborate.

| Pattern | Description | When To Use |
|---|---|---|
| Supervisor | One agent delegates to worker agents | Clear task decomposition |
| Hierarchical | Multi-level supervision tree | Large-scale systems |
| Collaborative | Agents discuss and reach consensus | Creative tasks, brainstorming |
| Sequential Pipeline | Agents process in order (A → B → C) | Document processing workflows |
| Debate / Adversarial | Agents argue for/against a position | Fact-checking, decision support |
| Swarm | Dynamic handoff between specialized agents | Customer service, routing |

```
Supervisor Multi-Agent Pattern
┌─────────────────────────┐
│     Supervisor Agent     │
│  (Task routing + state)  │
└────┬───────┬────────┬────┘
     │       │        │
     ▼       ▼        ▼
┌────────┐┌────────┐┌────────┐
│Research││ Writer ││ Critic │
│ Agent  ││ Agent  ││ Agent  │
└────────┘└────────┘└────────┘
     │       │        │
     ▼       ▼        ▼
  [Tools]  [Tools]  [Tools]
```

### 5. Agent Orchestration Frameworks

| Framework | Creator | Architecture | Best For |
|---|---|---|---|
| LangGraph | LangChain | Stateful graphs with cycles | Complex workflows, custom control flow |
| CrewAI | CrewAI Inc. | Role-based agent crews | Multi-agent collaboration |
| AutoGen | Microsoft | Conversational agent groups | Research, conversational agents |
| OpenAI Assistants | OpenAI | Managed agent runtime | Quick prototyping with OpenAI models |
| Semantic Kernel | Microsoft | Enterprise AI orchestration | .NET / enterprise integration |
| Swarm (OpenAI) | OpenAI | Lightweight agent handoffs | Educational, simple multi-agent |

**LangGraph Example:**

```python
from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated

class AgentState(TypedDict):
    messages: Annotated[list, add_messages]
    next_step: str

def researcher(state: AgentState) -> AgentState:
    # Research agent logic
    ...

def writer(state: AgentState) -> AgentState:
    # Writer agent logic
    ...

def router(state: AgentState) -> str:
    # Route to next agent based on state
    ...

graph = StateGraph(AgentState)
graph.add_node("researcher", researcher)
graph.add_node("writer", writer)
graph.add_conditional_edges("researcher", router, {"write": "writer", "research": "researcher"})
graph.add_edge("writer", END)
graph.add_edge(START, "researcher")

app = graph.compile()
```

### 6. Prompt Engineering for Agents

Agent prompts require specific techniques beyond standard LLM prompting.

| Technique | Description | Example |
|---|---|---|
| Role Definition | Detailed persona with expertise scope | "You are a senior data analyst with 10 years of experience..." |
| Tool Instructions | Explicit guidance on when/how to use tools | "Use web_search when you need current information. Use calculator for math." |
| Output Formatting | Structured response requirements | "Always respond with: Thought, Action, Observation format" |
| Guardrail Prompts | Boundary conditions and refusal logic | "Never execute destructive operations. Always confirm before..." |
| Few-shot Trajectories | Example reasoning traces | Show full Thought → Action → Observation examples |
| Self-Reflection Prompts | Force the agent to evaluate its own output | "Before responding, verify your answer is supported by evidence." |

### 7. Agent Evaluation and Testing

| Evaluation Dimension | Metrics | Tools |
|---|---|---|
| Task Completion | Success rate, partial completion | Custom eval harnesses |
| Tool Use Accuracy | Correct tool selection, valid arguments | LangSmith, Braintrust |
| Reasoning Quality | Logical consistency, relevance | LLM-as-judge, human eval |
| Efficiency | Steps to completion, token usage | LangSmith tracing |
| Safety | Refusal rate, boundary adherence | Red-teaming, adversarial tests |
| Latency | Time to first token, total time | Custom benchmarks |
| Cost | Total tokens, API calls per task | Cost tracking dashboards |

**Testing strategies:**
- **Unit tests:** Test individual tools and functions in isolation
- **Trajectory tests:** Verify the agent takes expected reasoning paths
- **End-to-end tests:** Test full task completion with known answers
- **Regression tests:** Ensure new changes don't break existing behavior
- **Adversarial tests:** Prompt injection, jailbreak attempts, edge cases
- **Human evaluation:** Expert review of agent outputs and reasoning

### 8. Production Agent Patterns

| Pattern | Description |
|---|---|
| Human-in-the-loop | Agent pauses for human approval on critical actions |
| Fallback chains | Graceful degradation when primary agent fails |
| Rate limiting | Control API calls and token usage per request |
| Caching | Cache tool results and LLM responses for efficiency |
| Streaming | Stream agent reasoning and actions to the user in real-time |
| Checkpointing | Save agent state to resume interrupted workflows |
| Retry with backoff | Automatic retry on transient failures |
| Observability | Full tracing of agent reasoning, tool calls, and results |

```
Production Agent Architecture
┌────────────────────────────────────────────┐
│                 API Gateway                 │
│          (Auth, Rate Limiting)              │
└──────────────────┬─────────────────────────┘
                   ↓
┌──────────────────────────────────────────────┐
│              Agent Orchestrator               │
│  ┌──────────┐  ┌──────────┐  ┌────────────┐ │
│  │ Routing  │→ │  Agent   │→ │  Response   │ │
│  │ Layer    │  │  Engine  │  │  Formatter  │ │
│  └──────────┘  └────┬─────┘  └────────────┘ │
│                     │                         │
│         ┌───────────┼───────────┐            │
│         ↓           ↓           ↓            │
│    ┌─────────┐ ┌─────────┐ ┌─────────┐      │
│    │  Tools  │ │ Memory  │ │Guardrails│      │
│    └─────────┘ └─────────┘ └─────────┘      │
└──────────────────────────────────────────────┘
                   ↓
┌──────────────────────────────────────────────┐
│            Observability Layer                │
│   (LangSmith / LangFuse / Custom Tracing)    │
└──────────────────────────────────────────────┘
```

### 9. AI Safety and Guardrails for Agents

| Risk | Mitigation |
|---|---|
| Prompt injection | Input sanitization, system prompt hardening, sandwich defense |
| Tool misuse | Permission scoping, allowlists, confirmation gates |
| Hallucinated actions | Output validation, tool result verification |
| Infinite loops | Max iteration limits, timeout enforcement |
| Data leakage | PII filtering, output scanning |
| Excessive cost | Token budgets, rate limits, circuit breakers |
| Harmful content | Content moderation API, safety classifiers |

**Guardrail implementation layers:**
1. **Input guardrails** — Validate and sanitize user inputs before the agent sees them
2. **Execution guardrails** — Constrain which tools the agent can call and with what arguments
3. **Output guardrails** — Validate agent responses before returning to the user
4. **System guardrails** — Rate limits, timeouts, cost caps, kill switches

---

## 🛠️ Tools & Technologies

| Tool | Purpose |
|------|---------|
| LangGraph | Stateful agent workflow orchestration |
| CrewAI | Multi-agent role-based collaboration |
| AutoGen | Conversational multi-agent framework |
| LangChain | Agent primitives and tool integrations |
| LangSmith | Agent tracing, evaluation, and debugging |
| LangFuse | Open-source LLM observability |
| OpenAI Assistants API | Managed agent runtime with tools |
| Tavily | Search API designed for AI agents |
| E2B | Sandboxed code execution for agents |
| Guardrails AI | Input/output validation framework |
| Streamlit | Rapid UI for agent demos |
| FastAPI | Production API serving for agents |

---

## 📚 Resources

See [resources.md](./resources.md) for full list.

| Resource | Type | Link |
|----------|------|------|
| LangGraph Documentation | Official Docs | https://langchain-ai.github.io/langgraph/ |
| CrewAI Documentation | Official Docs | https://docs.crewai.com/ |
| AutoGen Documentation | Official Docs | https://microsoft.github.io/autogen/ |
| Building Agentic RAG (DeepLearning.AI) | Free Course | https://www.deeplearning.ai/short-courses/building-agentic-rag-with-llamaindex/ |
| AI Agents in LangGraph (DeepLearning.AI) | Free Course | https://www.deeplearning.ai/short-courses/ai-agents-in-langgraph/ |
| Multi AI Agent Systems (DeepLearning.AI) | Free Course | https://www.deeplearning.ai/short-courses/multi-ai-agent-systems-with-crewai/ |

---

## 🏋️ Exercises

See the [exercises/](./exercises/) folder for:
- `01_react_agent.ipynb` — Build a ReAct agent from scratch using only an LLM and tools
- `02_function_calling.ipynb` — Implement OpenAI function calling with multiple tools
- `03_memory_systems.ipynb` — Add short-term and long-term memory to a conversational agent
- `04_langgraph_workflows.ipynb` — Build a stateful agent workflow with branching and cycles
- `05_multi_agent_basics.ipynb` — Create a two-agent system with supervisor routing
- `06_agent_evaluation.ipynb` — Evaluate agent performance with trajectory and outcome metrics

---

## 🛠️ Mini Projects

1. **ReAct Search Agent** — An agent that answers questions by searching the web, reasoning about results, and synthesizing answers with citations
2. **Personal Knowledge Agent** — A conversational agent with persistent memory that remembers user preferences and past interactions across sessions
3. **Code Debugging Agent** — An agent that reads Python code, identifies bugs using code execution, and suggests fixes with explanations

---

## 🏆 Major Projects

### Project 1: AI Research Assistant

Build a multi-agent system that autonomously researches any topic, fact-checks findings, and produces a structured report.

**Agents:**
- **Planner Agent** — Decomposes the research question into subtopics and search queries
- **Researcher Agent** — Searches the web using Tavily API and extracts relevant information
- **Fact-Checker Agent** — Cross-references claims across multiple sources and flags contradictions
- **Writer Agent** — Compiles verified findings into a well-structured Markdown report with citations

**Technologies:**
- LangGraph for agent orchestration and state management
- Tavily Search API for web research
- OpenAI GPT-4o for reasoning and generation
- ChromaDB for storing and retrieving research notes
- Streamlit for the user interface

**Expected Learning Outcomes:**
- Design and implement a multi-agent workflow with shared state
- Handle inter-agent communication and task delegation
- Implement fact-checking and source verification pipelines
- Build production-quality agent UIs with streaming output

---

### Project 2: AI Business Analytics Agent

Build an intelligent analytics agent that connects to datasets, performs data analysis, generates visualizations, and delivers actionable business insights.

**Features:**
- Natural language interface for data questions ("What were our top products last quarter?")
- Automated Python code generation and execution for data analysis
- Dynamic chart and visualization generation using matplotlib/plotly
- Insight summarization with business recommendations
- Conversation memory for follow-up questions

**Technologies:**
- LangChain agents with Python REPL tool
- E2B sandbox for safe code execution
- OpenAI GPT-4o for reasoning and code generation
- Pandas and matplotlib for data manipulation and visualization
- FastAPI backend with Streamlit frontend

**Expected Learning Outcomes:**
- Build agents that generate and execute code safely in sandboxed environments
- Implement natural language to SQL/pandas query translation
- Create dynamic visualization pipelines driven by AI
- Handle error recovery when generated code fails

---

### Project 3: Multi-Agent Collaboration System

Build a system where specialized agents collaborate to complete complex tasks — for example, a software development team with a product manager, developer, code reviewer, and QA tester.

**Agents:**
- **Product Manager Agent** — Interprets user requirements and creates task specifications
- **Developer Agent** — Writes code based on specifications using code generation tools
- **Code Reviewer Agent** — Reviews generated code for bugs, style, and best practices
- **QA Tester Agent** — Generates and runs test cases against the code

**Technologies:**
- CrewAI for role-based agent orchestration
- OpenAI GPT-4o as the base LLM
- E2B for sandboxed code execution and testing
- LangSmith for tracing multi-agent interactions
- Git integration for version tracking of generated code

**Expected Learning Outcomes:**
- Design role-based multi-agent architectures with clear responsibilities
- Implement structured communication protocols between agents
- Build feedback loops where agents iteratively improve each other's outputs
- Trace, debug, and optimize multi-agent workflows in production

See [projects/](./projects/) for full project templates.

---

## ✅ Stage Completion Checklist

- [ ] Completed all 6 exercises
- [ ] Built the ReAct search agent
- [ ] Built the personal knowledge agent
- [ ] Built the code debugging agent
- [ ] Completed the AI Research Assistant project
- [ ] Completed the AI Business Analytics Agent project
- [ ] Completed the Multi-Agent Collaboration System project
- [ ] Pushed everything to GitHub

**Next Stage → [07 MLOps](../07-mlops/)**
