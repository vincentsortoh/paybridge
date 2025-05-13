# Paybridge

Paybridge is a modular and extensible platform designed to unify access to diverse collection and payment service providers through a command-pattern architecture. It supports dynamic parameter and response mapping, seamless provider onboarding, and a React + FastAPI-powered admin UI for managing commands, providers, and integrations.

---

## ✅ TODO List

### 🔧 Core Backend Enhancements
- [ ] Add structured logging across provider executions and command dispatch  
  - Include log levels (INFO, ERROR, DEBUG)  
  - Use standard Python `logging` or `structlog`
- [ ] Add request/response tracing per command execution
- [ ] Implement exception handling middleware (FastAPI)

### 🌐 React Admin Interface (Frontend)
- [ ] Scaffold ReactJS project (e.g., with Vite or Create React App)
- [ ] Build Sidebar Navigation  
  - [ ] Providers  
  - [ ] Commands  
  - [ ] Mappings
- [ ] Pages:
  - [ ] Add & configure new commands
  - [ ] Add & configure new providers
  - [ ] Assign commands to providers
  - [ ] Edit parameter and response mappings (UI form)
- [ ] Integrate with FastAPI backend  
  - [ ] Fetch providers and commands  
  - [ ] Post updates to mapping configurations

### ⚙️ Configuration & Utilities
- [ ] Add CLI to register and list providers/commands
- [ ] Add unit tests for parameter and response mappers
- [ ] Document expected folder structure for adding providers

### 📝 Documentation
- [ ] Add usage examples in README
- [ ] Explain command structure and dynamic loading mechanism
- [ ] Add developer onboarding steps (env setup, running locally)
