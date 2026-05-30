# Libraries to Learn
Caveat: This is a subjective list of libraries to learn, based on my experience and the current Python ecosystem. The importance and community levels are meant to provide a general sense of how widely used and supported each library is, but they may vary depending on your specific use case and interests. Always consider your own needs and project requirements when choosing which libraries to learn and use.
## Legend
**Importance**
| Symbol | Level | Description |
|---:|:---:|:---|
| 🔴 | High | essential or core libraries with broad impact |
| 🟠 | Important | widely used libraries worth learning |
| 🟡 | Useful | helpful libraries that solve specific problems |
| 🟢 | Standard | built-in Python modules or stable core tools |
| 🟣 | Emerging | newer libraries gaining traction |
| ⚪ | Niche | specialized libraries for narrower use cases |

**Community**
| Symbol | Level | Description |
|---:|:---:|:---|
| 🔵 | Massive | very large user base and ecosystem |
| 🟣 | Very strong | well-established, active community |
| 🟢 | Strong | reliable community and support |
| 🟡 | Active | growing and engaged user base |
| 🟠 | Growing | expanding community |
| ⚪ | Stable | steady support, often standard library |
| ⚫ | Small | niche or limited community |

## S-tier
**fastapi** - 🔴 High importance, 🔵 Massive community, async-first web framework built on Starlette and Pydantic.  
**numpy** - 🔴 High importance, 🔵 Massive community, numerical arrays and linear algebra foundation for scientific Python.  
**pandas** - 🔴 High importance, 🟣 Very strong community, tabular data analysis and manipulation library.  
**pathlib** - 🟢 Standard importance, ⚪ Stable community, object-oriented filesystem path handling.  
**pydantic** - 🔴 High importance, 🟢 Strong community, modern data validation and settings management with type hints.  
**polars** - 🟣 Emerging importance, 🟠 Growing community, fast Rust-backed DataFrame library often used as a pandas alternative.  
**python-dotenv** - 🟡 Useful importance, 🟢 Strong community, loads environment variables from .env files.  

## C
**cmath** - 🟢 Standard importance, ⚪ Stable community, complex math functions for Python.  
**cpython** - 🟢 Standard importance, 🔵 Massive community, reference Python implementation and C API.  
**numba** - 🟠 Important importance, 🟡 Active community, JIT compiler for speeding numeric Python code with LLVM.  

## CLI
**argparse** - 🟢 Standard importance, ⚪ Stable community, built-in command-line argument parsing.  
**rich** - 🟠 Important importance, 🟣 Very strong community, rich text and beautiful terminal formatting library.  
**textual** - 🟣 Emerging importance, 🟠 Growing community, TUI framework built on Rich for text-based apps.  
**typer** - 🟠 Important importance, 🟢 Strong community, modern CLI builder based on type hints and Click.  

## Concurrency
**anyio** - 🟠 Important importance, 🟡 Active community, async compatibility layer for asyncio and trio.  
**asyncio** - 🔴 High importance, 🟢 Strong community, standard library async I/O framework.  
**concurrent.futures** - 🟢 Standard importance, ⚪ Stable community, high-level thread and process pool API.  
**multiprocessing** - 🟢 Standard importance, ⚪ Stable community, process-based parallelism module.  
**queue** - 🟢 Standard importance, ⚪ Stable community, thread-safe queue implementation.  
**subprocess** - 🟢 Standard importance, ⚪ Stable community, spawn and manage external processes.  
**threading** - 🟢 Standard importance, ⚪ Stable community, thread-based concurrency primitives.  
**trio** - 🟠 Important importance, 🟡 Active community, alternate async framework focused on structured concurrency.  

# Computer Vision
**deepsort** - 🟡 Useful importance, 🟡 Active community, tracker for multi-object tracking often paired with detection models.  
**opencv** - 🔴 High importance, 🔵 Massive community, computer vision library for image/video processing and algorithm building.  
**pillow** - 🟢 Standard importance, 🟢 Strong community, Python Imaging Library fork for image opening, manipulating, and saving.  
**scikit-image** - 🟠 Important importance, 🟢 Strong community, image processing library for scientific computing.  
**torchvision** - 🟠 Important importance, 🟣 Very strong community, vision models and image utilities that complement PyTorch.  
**ultralytics** - 🟣 Emerging importance, 🟠 Growing community, user-friendly PyTorch-based object detection suite (YOLO).  

## Data Analytics
**missingno** - 🟡 Useful importance, 🟠 Growing community, visual missing data analysis for pandas.  
**pyarrow** - 🟠 Important importance, 🟡 Active community, Apache Arrow Python bindings for columnar data.  
**seaborn** - 🟠 Important importance, 🟣 Very strong community, statistical data visualization library built on matplotlib.  
**xarray** - 🟡 Useful importance, 🟢 Strong community, labeled multi-dimensional arrays for scientific data.  

## DB
**alembic** - 🟠 Important importance, 🟢 Strong community, database migration tool built for SQLAlchemy.  
**asyncpg** - 🟠 Important importance, 🟢 Strong community, high-performance PostgreSQL driver with async support.  
**duckdb** - 🟠 Important importance, 🟠 Growing community, in-process SQL OLAP database for local query workloads.  
**motor** - 🟠 Important importance, 🟡 Active community, async MongoDB driver for Tornado and asyncio.  
**peewee** - 🟡 Useful importance, 🟡 Active community, lightweight ORM for simpler relational database use cases.  
**psycopg3** - 🟠 Important importance, 🟡 Active community, modern PostgreSQL driver for Python with async support.  
**redis-py** - 🟠 Important importance, 🟢 Strong community, Python client for Redis key-value store.  
**sqlalchemy** - 🔴 High importance, 🟣 Very strong community, SQL toolkit and ORM for relational databases.  
**sqlmodel** - 🟠 Important importance, 🟠 Growing community, SQLAlchemy-based ORM with Pydantic model integration.  
**sqlite3** - 🟢 Standard importance, ⚪ Stable community, lightweight embedded SQL database included with Python.  
**tortoise-orm** - 🟡 Useful importance, 🟠 Growing community, async ORM inspired by Django models for asyncio apps.  

## Developer Tools
**cProfile** - 🟢 Standard importance, ⚪ Stable community, deterministic profiler for Python code.  
**coverage** - 🟠 Important importance, 🟢 Strong community, test coverage measurement tool for Python.  
**pytest-cov** - 🟡 Useful importance, 🟡 Active community, plugin to measure coverage in pytest runs.  
**uv** - 🟡 Useful importance, 🟣 Very strong community, ultra-fast asynchronous CLI for Python development.  

## Document Parsing
**beautifulsoup** - 🟠 Important importance, 🟣 Very strong community, HTML/XML parsing library for web scraping.  
**jinja** - 🟠 Important importance, 🟣 Very strong community, templating engine for Python web apps.  
**pypdf** - 🟠 Important importance, 🟡 Active community, PDF manipulation library for Python.  
**pymupdf** - 🟡 Useful importance, 🟡 Active community, PDF and document processing library.  
**sphinx** - 🟠 Important importance, 🟣 Very strong community, documentation generator for Python projects.  

## GraphQL
**graphene** - 🟡 Useful importance, 🟡 Active community, GraphQL framework for Python.  
**strawberry** - 🟣 Emerging importance, 🟡 Active community, modern GraphQL library using Python type hints.  

## HTTP
**aiohttp** - 🟠 Important importance, 🟡 Active community, async HTTP client/server library for Python.  
**aiortc** - 🟣 Emerging importance, 🟠 Growing community, WebRTC and real-time communication library for Python.  
**httpx** - 🟠 Important importance, 🟡 Active community, async-capable HTTP client library for Python.  
**python-socketio** - 🟠 Important importance, 🟡 Active community, Socket.IO client/server implementation for Python.  
**requests** - 🔴 High importance, 🔵 Massive community, user-friendly HTTP client still popular despite async alternatives.  
**websockets** - 🟠 Important importance, 🟡 Active community, library for building WebSocket servers and clients.  

## LLM
**deepeval** - ⚪ Niche importance, ⚫ Small community, evaluation library for large language model outputs.  
**langchain** - 🔴 High importance, 🟢 Strong community, framework for building applications with large language models.  
**langgraph** - 🟣 Emerging importance, 🟠 Growing community, graph-based orchestration for LLM pipelines.  
**llama-index** - 🟠 Important importance, 🟡 Active community, indexing layer for retrieval-augmented LLM applications.  
**openai** - 🔴 High importance, 🔵 Massive community, official Python client for OpenAI API access.  
**ragas** - 🟣 Emerging importance, 🟠 Growing community, retrieval-augmented generation framework for LLM apps.  
**trulens** - 🟡 Useful importance, 🟠 Growing community, tool for analyzing and interpreting model behavior and trustworthiness.  

## Logging
**logging** - 🟢 Standard importance, ⚪ Stable community, built-in logging framework for Python.  
**loguru** - 🟠 Important importance, 🟢 Strong community, simpler and more user-friendly Python logging alternative.  
**structlog** - 🟡 Useful importance, 🟡 Active community, structured logging library for JSON-compatible logs and event data.  

## ML
**keras** - 🟠 Important importance, 🟣 Very strong community, high-level neural network API that is now tightly integrated with TensorFlow.  
**lightgbm** - 🟠 Important importance, 🟡 Active community, fast gradient boosting framework for large-scale datasets.  
**matplotlib** - 🟠 Important importance, 🟣 Very strong community, plotting library for static charts and figure generation.  
**onnx** - 🟠 Important importance, 🟢 Strong community, interoperable format and runtime for exporting and running ML models across frameworks.  
**plotly** - 🟠 Important importance, 🟣 Very strong community, interactive plotting and dashboarding library for both web and notebooks.  
**pytorch** - 🔴 High importance, 🔵 Massive community, flexible deep learning framework with strong research adoption.  
**scikit-learn** - 🔴 High importance, 🔵 Massive community, classic machine learning library for classification, regression, and clustering.  
**spacy** - 🟠 Important importance, 🟢 Strong community, industrial-strength NLP library.  
**tensorflow** - 🔴 High importance, 🟣 Very strong community, production-ready deep learning framework; many now prefer PyTorch but it remains widely used.  
**transformers** - 🔴 High importance, 🟣 Very strong community, Hugging Face library for pretrained NLP and multimodal models.  
**whisper** - 🟡 Useful importance, 🟡 Active community, OpenAI speech-to-text library for automatic speech recognition.  
**xgboost** - 🟠 Important importance, 🟣 Very strong community, gradient boosting library for high-performance tree models.  

## Networking
**netifaces** - 🟡 Useful importance, ⚪ Stable community, network interface information for Python.  
**scapy** - 🟡 Useful importance, 🟡 Active community, packet manipulation library for networking tasks.  

## Packaging / Environment
**pip** - 🟢 Standard importance, 🔵 Massive community, Python package installer.  
**pipenv** - 🟡 Useful importance, 🟡 Active community, virtualenv/dependency manager with Pipfile support.  
**pipx** - 🟠 Important importance, 🟢 Strong community, installs and runs Python CLI tools in isolated environments.  
**poetry** - 🟠 Important importance, 🟢 Strong community, modern dependency manager and packaging tool for Python.  
**pypy** - 🟠 Important importance, ⚫ Small community, alternative Python interpreter focused on performance.  
**python3** - 🟢 Standard importance, 🔵 Massive community, Python 3 interpreter executable.  
**venv** - 🟢 Standard importance, ⚪ Stable community, lightweight virtual environment creation tool.  

## Serialization
**ijson** - 🟡 Useful importance, 🟡 Active community, incremental JSON parser for large streams.  
**json** - 🟢 Standard importance, 🔵 Massive community, built-in JSON encode/decode.  
**msgpack** - 🟠 Important importance, 🟡 Active community, binary serialization format for compact and fast data exchange.  
**orjson** - 🟠 Important importance, 🟠 Growing community, ultra-fast JSON serializer/deserializer for Python.  
**PyYAML** - 🟠 Important importance, 🟣 Very strong community, YAML serializer/parser for configuration and data files.  
**pickle** - 🟢 Standard importance, ⚪ Stable community, Python object serialization with built-in persistence.  
**tomllib** - 🟢 Standard importance, ⚪ Stable community, reads TOML config files without extra dependencies.  

## Standards
**collections** - 🟢 Standard importance, 🔵 Massive community, container datatypes like deque and Counter.  
**dataclass** - 🟢 Standard importance, ⚪ Stable community, decorator for boilerplate-free data classes.  
**datetime** - 🟢 Standard importance, 🔵 Massive community, date/time manipulation module.  
**decimal** - 🟢 Standard importance, ⚪ Stable community, decimal fixed-point arithmetic for financial use.  
**functools** - 🟢 Standard importance, 🟣 Very strong community, function tools like caching and partial application.  
**glob** - 🟢 Standard importance, 🔵 Massive community, pathname pattern matching.  
**heapq** - 🟢 Standard importance, ⚪ Stable community, heap queue algorithms.  
**itertools** - 🟢 Standard importance, 🔵 Massive community, iterator building blocks.  
**math** - 🟢 Standard importance, 🔵 Massive community, basic math functions.  
**os** - 🟢 Standard importance, 🔵 Massive community, operating system interfaces.  
**random** - 🟢 Standard importance, 🔵 Massive community, pseudo-random number generation.  
**re** - 🟢 Standard importance, 🔵 Massive community, regular expression support.  
**shutil** - 🟢 Standard importance, 🔵 Massive community, high-level file operations.  
**socket** - 🟢 Standard importance, 🟣 Very strong community, low-level networking API.  
**sys** - 🟢 Standard importance, 🔵 Massive community, Python runtime system utilities.  
**time** - 🟢 Standard importance, 🔵 Massive community, date/time manipulation module.  
**typing** - 🟢 Standard importance, 🔵 Massive community, type hint definitions and utilities.  
**uuid** - 🟢 Standard importance, ⚪ Stable community, UUID generation and handling.  

## Static Analysis
**mypy** - 🟠 Important importance, 🟢 Strong community, static type checker for Python.  
**pyright** - 🟠 Important importance, 🟢 Strong community, fast static type checker and language server for Python.  
**ruff** - 🔴 High importance, 🟠 Growing community, fast Python linter and formatter.  

## Testing/Metrics
**hypothesis** - 🟠 Important importance, 🟢 Strong community, property-based testing library for generating edge-case inputs.  
**pyinstrument** - 🟡 Useful importance, 🟡 Active community, statistical profiler for Python performance analysis.  
**pytest** - 🔴 High importance, 🔵 Massive community, popular testing framework for Python.  
**pytest-asyncio** - 🟠 Important importance, 🟡 Active community, plugin for writing asyncio tests in pytest.  
**psutil** - 🟡 Useful importance, 🟣 Very strong community, process and system resource monitoring library.  
**timeit** - 🟢 Standard importance, ⚪ Stable community, simple timing utility for benchmarking short code snippets.  
**tracemalloc** - 🟢 Standard importance, ⚪ Stable community, memory tracing tool for diagnosing leaks.  
**unittest** - 🟢 Standard importance, ⚪ Stable community, built-in unit testing framework included with Python.  

## UI
**customtkinter** - ⚪ Niche importance, 🟠 Growing community, modern themed wrapper around Tkinter.  
**nicegui** - 🟣 Emerging importance, 🟠 Growing community, web UI framework for Python.  
**pyside6** - 🟠 Important importance, 🟡 Active community, Qt bindings for Python GUI apps.  
**streamlit** - 🟠 Important importance, 🟡 Active community, easy web app framework for data apps.  

## Web
**django** - 🔴 High importance, 🔵 Massive community, batteries-included web framework for full-stack applications.  
**flask** - 🔴 High importance, 🟣 Very strong community, lightweight web framework for building APIs and apps.  
**starlette** - 🟠 Important importance, 🟡 Active community, lightweight ASGI toolkit underpinning FastAPI.  
**uvicorn** - 🟠 Important importance, 🟢 Strong community, ASGI server commonly used for FastAPI and Starlette apps.  

## Others
**icecream** - 🟡 Useful importance, 🟠 Growing community, debugging library with friendly output.  
**numerizer** - ⚪ Niche importance, ⚫ Small community, parses text into numeric values.  
**pendulum** - 🟠 Important importance, 🟡 Active community, improved datetime library over the standard datetime module.  
**py2exe** - ⚪ Niche importance, ⚫ Small community, converts Python scripts to Windows executables.  
**pywin32** - ⚪ Niche importance, ⚫ Small community, Windows-specific support library for Python.  
**pygame** - 🟠 Important importance, 🟣 Very strong community, game development library for Python.  
**tqdm** - 🟠 Important importance, 🟣 Very strong community, progress bar utility for loops.  
**watchdog** - 🟡 Useful importance, 🟡 Active community, filesystem event monitoring library.  
