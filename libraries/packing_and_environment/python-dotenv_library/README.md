# 📚 python-dotenv library
`python-dotenv` reads secret and environment-specific values in a `.env` file into the python process.

## 🔬 Breakdown
|  | ⭐ (out of 5)| brief explanation |
|---|---|---|
| Usefulness | ⭐⭐⭐⭐⭐ | very useful for keeping secrets safe, pydantic.BaseSettings is better for larger projects |
| Community | ⭐⭐⭐⭐⭐ | strong community and widespread adoption | 
| Simplicity | ⭐⭐⭐⭐⭐ | extremely simple to understand, very minimalistic approach | 
| Robustness | ⭐⭐⭐⭐ | very robust, however no type validation and potentially truthy variable issues | 
| Performance | ⭐⭐⭐ | average performance, it is a synchronous disk-blocking operation | 

## 💿 Installation
With uv:
```bash
uv add python-dotenv
```
With pip:
```bash
pip install python-dotenv
```

## 🤔 How to Use
1. Create a `.env` file in your project root with key-value pairs `KEY=VALUE`.
2. Add `.env` to your `.gitignore`, **especially** if it
contains secrets like a password.
3. In your Python code, call `load_dotenv()` at the start of your application.
4. Access your variables via `os.getenv("KEY")`

## 🔋 Evaluation
`python-dotenv` is a focused library that solves a specific problem: making it easy to load environment variables from a file during development. It does this with minimal overhead and a simple API. However, it is not a full configuration management solution and does not provide features like validation, type coercion, or structured settings models. For projects that need those features, a library like `pydantic` or `dynaconf` might be more appropriate. But for many use cases, especially small projects or those already using environment variables, `python-dotenv` is an excellent choice for local development convenience.

Use it when you want the lowest-risk way to make local `.env` configuration behave like real environment variables without introducing a full configuration framework.

- Good for local development and test environments.
- Good for projects that already consume settings via `os.getenv()` or frameworks that rely on standard env vars.
- Not intended as a replacement for structured config systems, secret managers, or production-grade credentials storage.


---
## Background
Before diving into the library, its important to understand what environment variables are and the software design problem this library is attempting to solve.

### What are Environment Variables?
Explain what environment variables are
child processes take env var from parent and clone them
children CRUD independently from parents

<details>
<summary>CRUD env vars in bash/powershell</summary>
how to CRUD env in bash (linux) and ps (windows)
export to bring var to env
to make permanent `export key=value` must be in ~/.bashrc file and source ~/.bashrc
</details>

### 12 Factor Principles and Config
[12 factor principles](https://12factor.net/) specifically #3 [Config](https://12factor.net/config) and #4 [Backing services](https://12factor.net/backing-services) are relevant here. The 12 factor app design pattern emphasizes storing config in the environment, which is a common practice for 12 factor apps. This allows for separation of config from code and makes it easier to manage different environments (development, staging, production) without changing the codebase.

## Architectural Philosophy

At a systems level, `python-dotenv` addresses a configuration bottleneck created by two opposing needs:

- Developers need a simple way to define environment variables locally without manually exporting values in shell startup scripts.
- Applications need runtime configuration to live in the process environment (`os.environ`) so that libraries and frameworks behave consistently.

Instead of building a full settings framework, `python-dotenv` keeps the scope narrow:

- It parses lightweight `.env` files, not arbitrary structured config formats.
- It maps parsed key/value pairs directly into the process environment.
- It preserves the operating system's configuration boundary, letting the application use standard `os.getenv()`/`os.environ` semantics.

This design minimizes surface area and avoids introducing a second configuration API. The library is effectively a `file -> env` adapter that makes environment-driven apps easier to run in development.

The package solves a real structural issue in Python development workflows:

- Shell-based environment setup is fragile across platforms and shells (`bash`, `zsh`, `cmd.exe`, `PowerShell`).
- CI/CD systems and container workflows still expect settings via environment variables.
- Hard-coded config or project-specific settings files are easy to leak into version control.

`python-dotenv` gives developers a project-local place to keep values while still delivering them through the standard environment interface.

Because it reuses Python's own environment model, it is compatible with any code that already expects `os.environ` variables.

## Trade-off Matrix

| Feature | `python-dotenv` | `os.environ` only | `pydantic BaseSettings` |
|---|---|---|---|
| File-based local `.env` loading | ✅ | ❌ | ✅* |
| Uses standard process environment | ✅ | ✅ | ✅ |
| Minimal, file-to-env adapter | ✅ | ✅ | ❌ |
| Supports variable expansion / quoting | ✅ | ❌ | ✅* |
| Built for development / 12-factor style | ✅ | ❌ | ✅ |
| Dependency footprint | Very small | None | Small |
| Best for simple projects | ✅ | ❌ | ✅ |
| Best for typed validation and settings models | ❌ | ❌ | ✅ |

*`pydantic BaseSettings` can load `.env` files, but it is also a full validation and settings modeling layer rather than a dedicated file-to-env adapter.

## Dependency Ledger

- Runtime: Python interpreter only.
- Core dependency: Python standard library (`os`, `pathlib`, `io`, `typing`).
- OS integration: Python's `os` module uses the underlying platform environment variable APIs.
  - On Unix-like systems, this means the process environment table exposed by `setenv`/`putenv`.
  - On Windows, it uses the Win32 environment API behind Python's `os.environ`.
- File handling: simple text I/O, typically UTF-8 encoded `.env` files.
- External libraries: none. `python-dotenv` does not wrap C libraries like `libpq` or SDL.

## Practical notes

Because `python-dotenv` operates at the environment boundary, it is intentionally not a validation or settings type system. It is a plumbing library: it makes the environment available, then leaves validation and parsing to the application or secondary tools.
