# python-dotenv

`python-dotenv` is a lightweight bridge between file-based configuration and the process environment. It exists to solve the practical problem of local development configuration: keeping secret and environment-specific values in a project-local `.env` file while still exposing them as standard OS environment variables.

## Architectural Philosophy

At a systems level, `python-dotenv` addresses a configuration bottleneck created by two opposing needs:

- Developers need a simple way to define environment variables locally without manually exporting values in shell startup scripts.
- Applications need runtime configuration to live in the process environment (`os.environ`) so that libraries and frameworks behave consistently.

Instead of building a full settings framework, `python-dotenv` keeps the scope narrow:

- It parses lightweight `.env` files, not arbitrary structured config formats.
- It maps parsed key/value pairs directly into the process environment.
- It preserves the operating system's configuration boundary, letting the application use standard `os.getenv()`/`os.environ` semantics.

This design minimizes surface area and avoids introducing a second configuration API. The library is effectively a `file -> env` adapter that makes environment-driven apps easier to run in development.

## Why this library exists

The package solves a real structural issue in Python development workflows:

- Shell-based environment setup is fragile across platforms and shells (`bash`, `zsh`, `cmd.exe`, `PowerShell`).
- CI/CD systems and container workflows still expect settings via environment variables.
- Hard-coded config or project-specific settings files are easy to leak into version control.

`python-dotenv` gives developers a project-local place to keep values while still delivering them through the standard environment interface.

## Core mechanics

`python-dotenv` works in three small steps:

1. Read a `.env` file line-by-line.
2. Parse each assignment into a key and value, handling quotes and escapes.
3. Inject the result into Python's environment table via the standard `os` API.

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

## When to choose python-dotenv

Use it when you want the lowest-risk way to make local `.env` configuration behave like real environment variables without introducing a full configuration framework.

- Good for local development and test environments.
- Good for projects that already consume settings via `os.getenv()` or frameworks that rely on standard env vars.
- Not intended as a replacement for structured config systems, secret managers, or production-grade credentials storage.

## Practical note

Because `python-dotenv` operates at the environment boundary, it is intentionally not a validation or settings type system. It is a plumbing library: it makes the environment available, then leaves validation and parsing to the application or secondary tools.
