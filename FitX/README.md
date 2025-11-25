# FitX AI - Multi-Agent Fitness Assistant System

## 🏋️ Problem Statement

Fitness enthusiasts and beginners face multiple challenges:
- **Fragmented Information**: Fitness, nutrition, and shopping advice scattered across platforms
- **Lack of Personalization**: Generic advice doesn't account for individual goals, restrictions, or progress
- **Time-Consuming Planning**: Creating workout routines, meal plans, and finding right products is tedious
- **No Integrated Tracking**: Progress monitoring requires multiple apps and manual logging
- **Decision Paralysis**: Too many product choices without proper guidance

**Solution**: FitX AI is an intelligent multi-agent system that provides comprehensive fitness support through specialized AI agents working in harmony.

## 🎯 Value Proposition

- **Personalized Guidance**: Tailored workout and nutrition plans based on your profile
- **Expert Knowledge**: Multiple specialized agents with domain expertise
- **Integrated Shopping**: Direct product recommendations from Amazon, Flipkart, Myntra, Blinkit
- **Progress Tracking**: Automated logging and analytics of workouts and meals
- **Medical Context**: Health-aware advice that considers your medical conditions
- **Time Savings**: One platform for all fitness needs (estimated 10+ hours saved per week)

## 🏗️ Architecture

### Multi-Agent System Design (Using Google ADK)

```
                           ┌─────────────────────┐
                           │ Orchestrator Agent  │
                           │  (LlmAgent with     │
                           │   sub_agents)       │
                           └──────────┬──────────┘
                                      │
                    ┌─────────────────┼─────────────────┐
                    │                 │                 │
         ┌──────────▼─────────┐  ┌───▼────────┐  ┌────▼──────────┐
         │   Fitness Coach    │  │ Nutrition  │  │    Medical    │
         │   (LlmAgent)       │  │  Expert    │  │   Advisor     │
         │                    │  │ (LlmAgent) │  │  (LlmAgent)   │
         └────────────────────┘  └────────────┘  └───────────────┘
                    │                 │                 │
         ┌──────────▼─────────┐  ┌───▼────────────────────┐
         │ Progress Tracker   │  │  Shopping Assistant    │
         │   (LlmAgent)       │  │     (LlmAgent)         │
         └────────────────────┘  └────────────────────────┘
                    │                       │
         ┌──────────▼───────────────────────▼──────────┐
         │         Tool Layer (ADK Tools)              │
         │  - Custom shopping tools                    │
         │  - Progress logging tools                   │
         │  - Google Search                            │
         │  - Code Execution                           │
         └─────────────────────────────────────────────┘

         ┌─────────────────────────────────────────────┐
         │      Workflow Agents (Advanced)             │
         │  - SequentialAgent: Workout → Meal Plan     │
         │  - ParallelAgent: Multi-platform shopping   │
         └─────────────────────────────────────────────┘
```

### Agent Responsibilities

1. **Orchestrator Agent** (LlmAgent): Routes queries to specialized sub-agents
2. **Fitness Coach Agent** (LlmAgent): Creates workout plans, provides training guidance
3. **Nutrition Agent** (LlmAgent): Designs meal plans, provides dietary advice
4. **Medical Advisor Agent** (LlmAgent): Explains health concepts, discusses medical conditions
5. **Progress Tracker Agent** (LlmAgent): Logs workouts/meals, analyzes trends
6. **Shopping Assistant Agent** (LlmAgent): Recommends products across e-commerce platforms

### Advanced Workflows

- **SequentialAgent**: Combines workout planning → meal planning in sequence
- **ParallelAgent**: Searches equipment, food, and clothing simultaneously for efficiency

### Key Features Implemented (Kaggle Requirements)

✅ **Multi-Agent System**:
   - 5 specialized LlmAgents + 1 orchestrator
   - Sequential workflow (SequentialAgent)
   - Parallel workflow (ParallelAgent)
   - Agent-to-agent communication via sub_agents

✅ **Tools**:
   - Custom tools (6 functions for shopping & tracking)
   - Built-in Google Search tool
   - Code Execution tool (available)
   - Function calling with structured parameters

✅ **Sessions & Memory**:
   - InMemorySessionService for session management
   - MemoryBank integration for long-term memory
   - User profile context management
   - Conversation history tracking

✅ **Context Engineering**:
   - User profile context passed to all agents
   - Recent progress included in context
   - System instructions per agent role

✅ **Observability**:
   - Built-in ADK tracing
   - Progress logging with timestamps
   - Tool execution tracking


## 🙏 Acknowledgments

- Google's Agent Development Kit (ADK) team
- Kaggle's 5-Day AI Agents Intensive Course
- Google Gemini AI
- The AI agents community

## 📚 References

- [Google ADK Documentation](https://google.github.io/adk-docs/)
- [ADK Python GitHub](https://github.com/google/adk-python)
- [Kaggle Competition](https://www.kaggle.com/competitions/agents-intensive-capstone-project)

---

**Built with ❤️ using Google Agent Development Kit (ADK)**