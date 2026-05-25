# FuriosaAI Public Docs Snapshot

- fetched_at_kst: `2026-05-25T22:06:29.385571+09:00`
- docs_count: `11`

---

## Supported Models

- url: https://developer.furiosa.ai/latest/en/overview/supported_models.html
- category: `models`
- ok: `True`
- status_code: `200`
- text_chars: `1603`
- error: ``

### Excerpt

Supported Models
Supported Models
FuriosaAI’s software stack supports a wide range of Transformer-based models available on the Hugging Face Hub.
Below is a list of model architectures currently supported by the Furiosa SDK.
If your model is based on any of these architectures, you can use the
Furiosa SDK to compile, quantize, and run the model efficiently on
Furiosa’s NPUs.
Tip
Pre-compiled models are available in
Hugging Face Hub 🤗 - FuriosaAI organization
You can download and run them quickly with Furiosa-LLM.
Decoder-only Models (Text Generation)
Model Name
Architecture
Example Hugging Face Models
DeepSeek R1
LlamaForCausalLM
deepseek-ai/DeepSeek-R1-Distill-Llama-8B
deepseek-ai/DeepSeek-R1-Distill-Llama-70B
EXAONE 4.0
Exaone4ForCausalLM
LGAI-EXAONE/EXAONE-4.0-32B
LGAI-EXAONE/EXAONE-4.0-32B-FP8
Llama 3.1, Llama 3.3
LlamaForCausalLM
meta-llama/Llama-3.1-8B-Instruct
meta-llama/Llama-3.1-70B-Instruct
meta-llama/Llama-3.3-70B-Instruct
Solar 1.0
LlamaForCausalLM
upstage/SOLAR-10.7B-v1.0
upstage/SOLAR-10.7B-Instruct-v1.0
Qwen 2, Qwen 2.5
Qwen2ForCausalLM
Qwen/Qwen2.5-Coder-32B-Instruct
Qwen/Qwen2-32B
Qwen 3
Qwen3ForCausalLM
Qwen/Qwen3-0.5B-Instruct
Qwen/Qwen3-32B-Instruct
Pooling Models
Model Name
Architecture
Task
Example Hugging Face Models
Qwen 3 Embedding
Qwen3Model
Embedding
Qwen/Qwen3-Embedding-4B
Qwen/Qwen3-Embedding-8B
Qwen 3 Reranker
Qwen3ForSequenceClassification
Reranking
Qwen/Qwen3-Reranker-4B
Qwen/Qwen3-Reranker-8B
Planned Models for Future Releases
(The order of the models listed below indicate the priority of support.)
GPT-OSS
K-EXAONE
Solar Open
Qwen3 MoE
Qwen3 VL

---

## Release 2026.2

- url: https://developer.furiosa.ai/docs-dev/PR-3475/en/whatsnew/release-2026.2.html
- category: `release`
- ok: `True`
- status_code: `200`
- text_chars: `10480`
- error: ``

### Excerpt

Furiosa SDK Release 2026.2
Furiosa SDK Release 2026.2
We are happy to announce the release of
Furiosa SDK 2026.2
Building on the foundation laid in 2026.1, this release focuses on making production
deployments faster, easier to configure, and easier to scale out. We have improved
serving performance for
Qwen3
and
Exaone4
, removed most of the bucket-tuning
ceremony from artifact builds via
preset-based configuration
, introduced an
independent
Data Parallel (DP) Router
with a
prefix-aware
variant, enabled
prefix caching by default
, and shipped the first phase of the
Response API
(/v1/responses)
If you are upgrading from 2026.1, please also read the
🚨 Breaking Changes & Deprecations
section and the
Upgrading FuriosaAI’s Software
Highlights
Qwen3 and Exaone4 Performance Improvements
Two of the most frequently deployed model families on RNGD see meaningful throughput
improvements in this release, with per-request latencies held at 2026.1 levels.
Qwen3
artifacts ship with expanded prefill, decode, and append buckets (including
a 64k append bucket for Qwen3-32B-FP8) so more of the real-world request distribution
hits well-tuned kernels, and
Exaone4
gains more high-batch and append buckets
along with
Hybrid KV Cache Management
, which splits KV memory
into separate global-attention and sliding-window pools and reclaims sliding-window
blocks as soon as they fall outside the active window — reducing memory waste and
lifting effective concurrency on long-context workloads.
Across a sweep of input length, output length, and concurrency, tokens/second
throughput improved by
74.9% on average over 2026.1
, rising to
84.8%
in the
low-concurrency regime (concurrency below 64), while TTFT and TPOT remain in line
with the 2026.1 baseline.
Per-Model Bucket Presets
Good bucket configuration — the set of prefill, decode, and append bucket sizes
an artifact is compiled for — is one of the highest-leverage knobs for serving
performance, and also one of the hardest to tune by hand. In 2026.2,
ArtifactBuilder
absorbs that complexity: every supported model ships with
per-model bucket presets
, tuned by the Furiosa team to match each model’s
architecture and cover its full maximum context, and applied automatically at
build time.
The design goal is simple —
the default build should produce the best artifact
for typical serving workloads
, without requiring the user to reason about
bucketization at all:
# Build an artifact for Qwen3-32B-FP8 and write it to ./Qwen3-32B-FP8
furiosa-llm
build
Qwen/Qwen3-32B-FP8
-tp
./Qwen3-32B-FP8
Explicit bucket arguments are still supported and take precedence, so workload-
specific tuning remains available for users who need it.
Data Parallel Router with Prefix-Aware Routing
2026.2 introduces a first-class
Data Parallel (DP) Router
for horizontally scaled
deployments. The router sits in front of the frontend and dispatches each request to
a DP replica before any engine-local scheduling happens, so clients see a single
entry point while each replica runs its own scheduler independently.
Two routing policies are available.
round_robin
distributes requests evenly
across replicas;
prefix_aware
inspects the tokenized prefix and prefers the
replica that already holds matching prefix cache entries — important for workloads
with shared leading tokens, such as chatbots with long system prompts or RAG systems,
where naive round-robin scatters shared prefixes across replicas and destroys cache
locality. The policy is selected via
--data-parallel-routing-policy
, and defaults
prefix_aware
when prefix caching is enabled and
round_robin
otherwise:
# Explicitly use prefix-aware routing
furiosa-llm
serve
<model>
--data-parallel-size
<N>
--data-parallel-routing-policy
<policy>
Prefix Caching Is Now On by Default
Prefix caching was introduced in 2026.1 behind an opt-in flag. After a release of
production use and several correctness and performance improvements, it is now
enabled by default
in 2026.2. You no longer need any flag to benefit from it.
Alongside the default flip, we landed several refinements:
Prefix cache hit deferral
maximizes the cache hit rate by briefly deferring
requests that are about to match an in-flight prefix, instead of kicking them off to
a fresh prefill.
Prefix caching is applied to decoded outputs
as well, so multi-turn
conversations benefit from the cache even on the continuation side.
If you need to disable prefix caching for a specific deployment — for example, for
workloads that rarely share prefixes across requests, or for benchmarking runs where
cache-hit variance would distort the measurements — pass
--no-enable-prefix-caching
furiosa-llm
serve
<model>
--no-enable-prefix-caching
Response API (Phase 1)
2026.2 adds initial support for the
Response API
/v1/responses
. The Response API is OpenAI’s newer, more expressive alternative to
Chat Completions, and this release covers enough of the surface area to be useful for
straightforward request/response flows.
This is labeled
Phase 1
inten

---

## RNGD Overview

- url: https://developer.furiosa.ai/latest/en/overview/rngd.html
- category: `hardware`
- ok: `True`
- status_code: `200`
- text_chars: `2548`
- error: ``

### Excerpt

FuriosaAI RNGD
FuriosaAI RNGD
RNGD is FuriosaAI’s second-generation Neural Processing Unit (NPU) designed to accelerate deep learning inference.
The NPU natively supports a broad spectrum of workloads, including high-performance Large Language Models (LLMs), multi-modal models, and vision-based neural networks.
RNGD implements the Tensor Contraction Processor (TCP), a novel architecture designed to natively execute complex tensor contractions—the core mathematical operations underlying modern deep learning—directly in hardware.
By leveraging this paradigm, the NPU maximizes both compute utilization and energy efficiency.
Fabricated on TSMC’s 5nm process node and operating at a 1.0 GHz clock frequency, RNGD delivers high-throughput execution across diverse precision formats, achieving 256 TFLOPS for BF16, 512 TFLOPS for FP8, 512 TOPS for INT8, and 1024 TOPS for INT4 workloads.
To sustain these compute throughputs without memory bottlenecks, the chip integrates two HBM3 modules that provide an aggregate memory bandwidth of 1.5 TB/s.
Furthermore, it interfaces with the host via PCIe Gen5 x16, ensuring low-latency data movement.
In addition to its core compute capabilities, RNGD seamlessly integrates into cloud-native and multi-tenant environments like Kubernetes.
By implementing Single Root I/O Virtualization (SR-IOV), the system allows a single physical chip to be partitioned into 2, 4, or 8 independent NPU instances.
Each virtual instance operates with strict hardware isolation, utilizing its own dedicated compute cores and private memory bandwidth to guarantee deterministic latency for co-located workloads.
For a detailed technical analysis of the TCP architecture and the RNGD implementation, please refer to the following publications:
TCP: A Tensor Contraction Processor for AI Workloads (ISCA 2024)
PDF
FuriosaAI RNGD: A Tensor Contraction Processor for Sustainable AI Computing (Hotchips 2024)
Tensor Contraction Processor: The First Future-Proof AI Chip Architecture
RNGD Hardware Specification
Architecture
Tensor Contraction Processor
Process Node
TSMC 5nm
Frequency
1.0 GHz
BF16
256 TFLOPS
FP8
512 TFLOPS
INT8
512 TOPS
INT4
1024 TOPS
Memory Bandwidth
HBM3 1.5TB/s
Memory Capacity
HBM3 48GB
On-Chip SRAM
256MB
Interconnect Interface
PCIe Gen5 x16
Thermal Solution
Passive
Thermal Design Power (TDP)
150W
Power Connector
12VHPWR
Form Factor
PCIe dual-slot full-height 3/4 Length
Multi-Instance Support
Virtualization Support
Yes
SR-IOV
8 Virtual Functions
ECC Memory Support
Yes
Secure Boot with Root of Trust
Yes

---

## Software Stack

- url: https://developer.furiosa.ai/latest/en/overview/software_stack.html
- category: `software`
- ok: `True`
- status_code: `200`
- text_chars: `3602`
- error: ``

### Excerpt

FuriosaAI’s Software Stack
FuriosaAI’s Software Stack
FuriosaAI offers a streamlined software stack that enables the FuriosaAI NPU to
be used across various applications and environments.
Here, we outline the software stack provided by FuriosaAI, explaining
the roles of each component, along with guidelines and tutorials.
The following diagram shows the software stack provided by FuriosaAI.
Kernel Driver, Firmware, and PE Runtime
The kernel device driver enables the Linux operating system to recognize NPU devices and
expose them as Linux device files.
The firmware runs on the NPU and provides low-level APIs to the PE Runtime
(PERT) that runs on the Processing Element (PE).
PERT is responsible for communicating with the host’s runtime, as well as
scheduling and managing the resources of PEs to execute NPU tasks.
Furiosa Compiler
The Furiosa Compiler optimizes model graphs and generates executable programs
for the NPU.
It performs several optimizations, including graph-level optimizations, operator
fusion, optimization of memory allocations, scheduling, and optimization of
cross-layer data movements.
A single model can be compiled into multiple executables, depending on
the model’s architecture and application requirements.
When using FuriosaAI’s backend for
torch.compile()
FuriosaBackend
), or
the
furiosa-llm
package, the Furiosa Compiler is used transparently to
generate NPU executables.
Furiosa Runtime
The Runtime loads the executables generated by the Furiosa compiler and runs
them on the NPU.
The Runtime is responsible for scheduling NPU programs and allocating memory
on both the NPUs and the host RAM.
Additionally, the Runtime supports the use of multiple NPUs and provides a
unified entry point for running models across multiple NPUs seamlessly.
Furiosa Model Compressor (Quantizer)
The Furiosa Model Compressor is a toolkit for model calibration and quantization.
Model quantization is a powerful technique to reduce memory usage, computation
cost, inference latency, and power consumption.
The Furiosa Model Compressor provides post-training quantization methods, such as:
BF16 (W16A16)
INT8 Weight-Only (W8A16) (Planned)
FP8 (W8A8)
INT8 SmoothQuant (W8A8) (Planned)
INT4 Weight-Only (W4A16 AWQ / GPTQ) (Planned)
Furiosa-LLM
Furiosa-LLM is a high-performance inference engine for LLM models, such as Llama and GPT-J.
The key features of Furiosa-LLM include:
vLLM-compatible API, for seamless integration with vLLM-based workflows;
PagedAttention, for optimized memory usage for attention computation;
Continuous batching, improving throughput by dynamically grouping inference requests;
Hugging Face Hub
support,
simplifying access to pre-trained models;
OpenAI-compatible API server, enabling easy deployment using familiar APIs.
For more information, please refer to the
Furiosa-LLM
section.
Kubernetes Support
Kubernetes, an open-source platform for managing containerized applications
and services, is widely adopted by organizations for its powerful capabilities
in deploying, scaling, and automating containerized workloads.
The FuriosaAI software stack offers native integration with Kubernetes,
enabling seamless deployment and management of AI applications within
Kubernetes environments.
FuriosaAI’s device plugin enables Kubernetes clusters to recognize FuriosaAI’s
NPUs and schedule them for workloads that require them.
This integration simplifies the deployment of AI workloads with FuriosaAI NPUs,
ensuring efficient resource utilization and scalability.
For more information about Kubernetes support, please refer to
the
Cloud Native Toolkit
section.

---

## Roadmap

- url: https://developer.furiosa.ai/latest/en/overview/roadmap.html
- category: `roadmap`
- ok: `True`
- status_code: `200`
- text_chars: `2750`
- error: ``

### Excerpt

Roadmap
Roadmap
FuriosaAI regularly publishes its software with new features, performance improvements, and expanded hardware support.
This page shows the forward-looking roadmap of ongoing & upcoming projects and when they are expected to land, broken down by areas on
our software stack
Note
The latest release is 2026.2.0. You can find the release notes
here
Upcoming Releases 2026 Q1 - Q2
🔨 Qwen3 MoE, GPT-OSS, K-EXAONE, Solar Open model support
🔨 Qwen3 VL and multi-modal model support
🔨 KV cache offloading support
✅ Response API support
🔨 Speculative decoding support
🔨 PyTorch eager mode support
2025 Q3 - Q4
Furiosa-LLM
✅ Hybrid batching support (i.e., chunked prefill or inflight-batching)
✅ Exaone4, Qwen3 support
✅ Guided-decoding support (libguidance, xgrammar backends)
✅ Tool-calling support
✅ Prefix-caching support
✅ Pooling Model support (embedding, score, and rank)
✅ Fine-tuned model support
✅ Tensor Parallelism support Phase 2: Inter-chip
✅ Hugging Face Hub support
✅ Pre-compiled artifacts on Hugging Face Hub
✅ Qwen2 and Qwen2.5 model support
✅ EXAONE3 model support
✅ API Key based authentication support
✅ Harmony response format support
Quantization
✅ Fine-grained FP8 Quantization (dynamic quantization, mixed quantization)
Distributed & Scalable Inference
✅ llm-d integration
✅ NPU operator support for Kubernetes
✅ DRA (Dynamic Resource Allocation) support for Kubernetes
2025 Q1 - Q2
✅ Tool-calling support in Furiosa-LLM (2025.1.0 release)
✅ Device remapping support (e.g., /dev/rngd/npu2pe0-3 -> /dev/rngd/npu0pe0-3) for container (2025.1.0 release)
✅ Automatic configuration for the maximum KV-cache memory allocation (2025.1.0 release)
✅ Min-p sampling support (2025.1.0 release)
✅ Chunked Prefill support in Furiosa-LLM (planned for 2025.2.0 release)
✅ Chat API support in Furiosa-LLM (planned for 2025.2.0 release)
✅ Reasoning parser support (2025.2.0 release)
✅ Torch 2.5.1 support (2025.2.0 release)
✅ Python 3.11 and 3.12 support (2025.2.0 release)
✅ Support for building bfloat16, float16, and float32 models to model artifact without quantization (2025.2.0 release)
✅ Metrics endpoint (
/metrics/
) support in Furiosa-LLM (2025.2.0 release)
✅ Model artifact support in Huggingface Hub (2025.2.0 release)
✅ Sampling parameter “logprobs” support (2025.2.0 release)
✅ Container Runtime and Container Interface Device (CDI) support (2025.2.0 release)
2024 Q4
✅ Language Model Support: CodeLLaMA2, Vicuna, Solar, EXAONE-3.0 (2024.2.0 release)
✅ Vision Model Support: MobileNetV1, MobileNetV2, ResNet152, ResNet50, EfficientNet, YOLOv8m, etc (2024.2.0 release)
✅ Tensor Parallelism support Phase 1: Intra-chip (2024.2.0 release)
✅ Torch 2.4.1 support (2024.2.0)
✅ Huggingface Optimum integration (2024.2.0 release)

---

## Furiosa LLM Intro

- url: https://developer.furiosa.ai/latest/en/furiosa_llm/intro.html
- category: `serving`
- ok: `True`
- status_code: `200`
- text_chars: `1653`
- error: ``

### Excerpt

Furiosa-LLM
Furiosa-LLM
Furiosa-LLM is a high-performance inference engine for LLM and multi-modal
LLM models.
Furiosa-LLM offers state-of-the-art serving efficiency and optimizations.
Key features of Furiosa-LLM include:
vLLM-compatible API (LLM, LLMEngine, AsyncLLMEngine API)
Efficient KV cache management with PagedAttention
Continuous batching of incoming requests
Quantization: FP8 (Planned: INT4, INT8, GPTQ, AWQ)
Support for data, tensor, and pipeline parallelism across multiple NPUs
OpenAI-compatible API server
Various decoding algorithms: greedy search, top-k/top-p, and speculative decoding (planned for 2026.3)
Tool calling and reasoning parser support
Structured output generation (choice, regex, json schema, grammar)
Chunked Prefill
Integration with Hugging Face models and hub support
Hugging Face PEFT support (planned)
Documentation
Quick Start with Furiosa-LLM
: A quick start guide to Furiosa-LLM
OpenAI-Compatible Server
: Details about the OpenAI-compatible server and its features
Responses API
: Guide to the OpenResponses-compatible Responses API
Tool Calling
: Guide to tool calling with parsers and choice options
Structured Output
: Guide to structured output generation
Prefix Caching
: Guide to prefix caching for improved performance
Hybrid KV Cache Management
: Understanding hybrid KV cache management
Model Preparation
: How to prepare LLM models to be served by Furiosa-LLM
Model Parallelism
: A guide to model parallelism in Furiosa-LLM
API Reference
: Python API reference for Furiosa-LLM
Examples
: Examples of using Furiosa-LLM
Deploying Furiosa-LLM on Kubernetes
: A guide to deploying Furiosa-LLM on Kubernetes

---

## Cloud Native Toolkit

- url: https://developer.furiosa.ai/latest/en/cloud_native_toolkit/intro.html
- category: `cloud_native`
- ok: `True`
- status_code: `200`
- text_chars: `600`
- error: ``

### Excerpt

Cloud Native Toolkit
Cloud Native Toolkit
FuriosaAI Cloud Native Toolkit is a software stack to enable FuriosaAI’s NPU product in Kubernetes and container ecosystems.
It simplifies the deployment and management of NPU-accelerated workloads in cloud-native infrastructure,
allowing developers to build containerized applications that integrate seamlessly with enterprise cloud-native platforms and cloud management frameworks.
Note
This diagram may include components that have not been publicly released yet. These components are currently in development and will be available in an upcoming release.

---

## System Management Interface

- url: https://developer.furiosa.ai/latest/en/device_management/system_management_interface.html
- category: `management`
- ok: `True`
- status_code: `200`
- text_chars: `760`
- error: ``

### Excerpt

Furiosa SMI
Furiosa SMI
Furiosa System Management Interface (furiosa-smi) provides the capability to manage and monitor FuriosaAI NPU products.
The
furiosa-smi
is command line interface (CLI) version of the interface based on the top of the Furiosa SMI Library.
The CLI tool allows users and/or administrators to access npu information, system topology, utilization, and performance data.
Visit
Furiosa SMI CLI
page for more information.
The Furiosa System Management Interface Library provides C-based programmatic interface with Go, Rust, Python bindings.
It is designed for developers to integrate the Furiosa NPU into their applications, platforms and infrastructure.
Visit
Furiosa SMI Library
page for more information.
Furiosa SMI CLI
Furiosa SMI Library

---

## Hugging Face FuriosaAI Org

- url: https://huggingface.co/furiosa-ai
- category: `huggingface`
- ok: `True`
- status_code: `200`
- text_chars: `3619`
- error: ``

### Excerpt

AI & ML interests
None defined yet.
Recent Activity
hyunsikc
updated
a model
about 1 month ago
furiosa-ai/EXAONE-4.0-32B-FP8
hyunsikc
updated
a model
about 1 month ago
furiosa-ai/Qwen3-32B-FP8
hyunsikc
updated
a model
about 1 month ago
furiosa-ai/Llama-3.3-70B-Instruct
View all activity
Papers
ParallelBench: Understanding the Trade-offs of Parallel Decoding in
Diffusion LLMs
View all Papers
Team members
Organization Card
Community
About org cards
FuriosaAI develops data center AI accelerators. Our RNGD (pronounced "Renegade") accelerator, currently sampling,
excels at high-performance inference for LLMs and agentic AI.
Get started fast with common inference tasks on RNGD
using these pre-compiled popular Hugging Face models – no manual conversion or quantization needed. Requires Furiosa SDK 2025.2 or later on a server with RNGD accelerator.
Need a model with custom configurations? Compile it yourself using our
Model Preparation Workflow
on Furiosa Docs.
Visit
Supported Models
in the SDK documentation
for more information and learn more about RNGD at
https://furiosa.ai/rngd
Featured Pre-compiled models for v2026.1
Please check out the collection of models at
https://huggingface.co/furiosa-ai/collections
Pre-compiled Model
Description
Base Model
Support Version
furiosa-ai/EXAONE-4.0-32B-FP8
FP8
LGAI-EXAONE/EXAONE-4.0-32B-FP8
>= 2026.1
furiosa-ai/Llama-3.1-8B-Instruct
BF16
meta-llama/Llama-3.1-8B-Instruct
>= 2025.2
furiosa-ai/Llama-3.3-70B-Instruct
BF16
meta-llama/Llama-3.3-70B-Instruct
>= 2025.3
furiosa-ai/Qwen2.5-0.5B-Instruct
BF16
Qwen/Qwen2.5-0.5B-Instruct
>= 2026.1
furiosa-ai/Qwen3-Embedding-8B
BF16
Qwen/Qwen3-Embedding-8B
>= 2026.1
furiosa-ai/Qwen3-Reranker-8B
BF16
Qwen/Qwen3-Reranker-8B
>= 2026.1
furiosa-ai/Qwen3-32B-FP8
FP8
Qwen/Qwen3-32B-FP8
>= 2026.1
Examples
First, install the pre-requisites by following
Installing Furiosa-LLM
Then, run the following command to start the Furiosa-LLM server with the Llama-3.1-8B-Instruct-FP8 model:
furiosa-llm serve furiosa-ai/EXAONE-4.0-32B-FP8
For reasoning models like DeepSeek-R1-Distill-Llama-8B, you can enable the reasoning mode with a proper reasoning parser:
furiosa-llm serve furiosa-ai/EXAONE-4.0-32B-FP8 \
--enable-reasoning --reasoning-parser exaone4
Once your server has launched, you can query the model with input prompts:
curl http://localhost:8000/v1/chat/completions \
"Content-Type: application/json"
"model": "EMPTY",
"messages": [{"role": "user", "content": "What is the capital of France?"}]
| python -m json.tool
You can also learn more about usages from
Quick Start with Furiosa-LLM
Collections
Qwen 2.5
Text Generation
Updated
Aug 22, 2025
Text Generation
Updated
Aug 28, 2025
Text Generation
Updated
Sep 5, 2025
Qwen 2.5 Coder
Text Generation
Updated
Sep 5, 2025
Text Generation
Updated
Jul 31, 2025
Text Generation
Updated
Aug 28, 2025
Qwen 2.5
Text Generation
Updated
Aug 22, 2025
Text Generation
Updated
Aug 28, 2025
Text Generation
Updated
Sep 5, 2025
Qwen 2.5 Coder
Text Generation
Updated
Sep 5, 2025
Text Generation
Updated
Jul 31, 2025
Text Generation
Updated
Aug 28, 2025
View 6 collections
spaces
Sort:
Recently updated
Mot
Run a MOT demo for object tracking
Ocr
Extract text from images
models
Sort:
Recently updated
Text Generation
Updated
Apr 13
Text Generation
Updated
Apr 13
113
Text Generation
Updated
Apr 13
344
Text Generation
Updated
Apr 13
334
Sentence Similarity
Updated
Apr 13
Text Classification
Updated
Apr 13
Text Generation
Updated
Apr 13
105
Text Generation
Updated
Sep 19, 2025
Text Generation
Updated
Sep 19, 2025
Text Generation
Updated
Sep 5, 2025
View 23
models
datasets
None public yet

---

## Hugging Face FuriosaAI Models

- url: https://huggingface.co/furiosa-ai/models
- category: `huggingface_models`
- ok: `True`
- status_code: `200`
- text_chars: `1280`
- error: ``

### Excerpt

AI & ML interests
None defined yet.
Recent Activity
hyunsikc
updated
a model
about 1 month ago
furiosa-ai/EXAONE-4.0-32B-FP8
hyunsikc
updated
a model
about 1 month ago
furiosa-ai/Qwen3-32B-FP8
hyunsikc
updated
a model
about 1 month ago
furiosa-ai/Llama-3.3-70B-Instruct
View all activity
Papers
ParallelBench: Understanding the Trade-offs of Parallel Decoding in
Diffusion LLMs
View all Papers
Team members
furiosa-ai
's models
Sort:
Recently updated
Text Generation
Updated
Apr 13
Text Generation
Updated
Apr 13
113
Text Generation
Updated
Apr 13
344
Text Generation
Updated
Apr 13
334
Sentence Similarity
Updated
Apr 13
Text Classification
Updated
Apr 13
Text Generation
Updated
Apr 13
105
Text Generation
Updated
Sep 19, 2025
Text Generation
Updated
Sep 19, 2025
Text Generation
Updated
Sep 5, 2025
Text Generation
Updated
Sep 5, 2025
Text Generation
Updated
Sep 5, 2025
Text Generation
Updated
Aug 28, 2025
Text Generation
Updated
Aug 28, 2025
Text Generation
Updated
Aug 28, 2025
Text Generation
Updated
Aug 27, 2025
Text Generation
Updated
Aug 27, 2025
Text Generation
Updated
Aug 27, 2025
Text Generation
Updated
Aug 22, 2025
Text Generation
Updated
Jul 31, 2025
Text Generation
Updated
Jul 31, 2025
Text Generation
Updated
Jul 31, 2025
Text Generation
Updated
Jul 31, 2025

---

## Hugging Face FuriosaAI Collections

- url: https://huggingface.co/furiosa-ai/collections
- category: `huggingface_collections`
- ok: `True`
- status_code: `200`
- text_chars: `1736`
- error: ``

### Excerpt

AI & ML interests
None defined yet.
Recent Activity
hyunsikc
updated
a model
about 1 month ago
furiosa-ai/EXAONE-4.0-32B-FP8
hyunsikc
updated
a model
about 1 month ago
furiosa-ai/Qwen3-32B-FP8
hyunsikc
updated
a model
about 1 month ago
furiosa-ai/Llama-3.3-70B-Instruct
View all activity
Papers
ParallelBench: Understanding the Trade-offs of Parallel Decoding in
Diffusion LLMs
View all Papers
Team members
furiosa-ai
's collections
Qwen 2.5
Text Generation
Updated
Aug 22, 2025
Text Generation
Updated
Aug 28, 2025
Text Generation
Updated
Sep 5, 2025
EXAONE 3.5
Text Generation
Updated
Jul 31, 2025
Text Generation
Updated
Jul 31, 2025
Llama 3.3
Text Generation
Updated
Apr 13
113
Text Generation
Updated
Aug 28, 2025
Qwen 2.5 Coder
Text Generation
Updated
Sep 5, 2025
Text Generation
Updated
Jul 31, 2025
Text Generation
Updated
Aug 28, 2025
DeepSeek R1
Text Generation
Updated
Sep 19, 2025
Text Generation
Updated
Sep 19, 2025
Text Generation
Updated
Aug 27, 2025
Text Generation
Updated
Sep 5, 2025
Llama 3.1
Text Generation
Updated
Apr 13
344
Text Generation
Updated
Jul 31, 2025
Qwen 2.5
Text Generation
Updated
Aug 22, 2025
Text Generation
Updated
Aug 28, 2025
Text Generation
Updated
Sep 5, 2025
Qwen 2.5 Coder
Text Generation
Updated
Sep 5, 2025
Text Generation
Updated
Jul 31, 2025
Text Generation
Updated
Aug 28, 2025
EXAONE 3.5
Text Generation
Updated
Jul 31, 2025
Text Generation
Updated
Jul 31, 2025
DeepSeek R1
Text Generation
Updated
Sep 19, 2025
Text Generation
Updated
Sep 19, 2025
Text Generation
Updated
Aug 27, 2025
Text Generation
Updated
Sep 5, 2025
Llama 3.3
Text Generation
Updated
Apr 13
113
Text Generation
Updated
Aug 28, 2025
Llama 3.1
Text Generation
Updated
Apr 13
344
Text Generation
Updated
Jul 31, 2025
