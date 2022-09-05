To what extent is cyclomatic complexity relevant when developing object-oriented code?

Cyclomatic complexity is really important. Having many branches in your code not only makes your code more complex and harder to read, but it also slows it down. The CPU has to do branch prediction (Branch predictor: How many "if"s are too many? Including x86 and M1 benchmarks!, 2022) and depending on the CPU architecture, it would try and figure out which branch is going to execute, and sometimes it would execute all branches and get rid of the wrong branch, which is not great. The fewer branches, the faster your code is going to be and the less work your CPU has to do.

Especially for GPUs, where they have thousands of cores, having branches would stall the GPU pipeline and tank the performance (Chapter 34. GPU Flow-Control Idioms, 2022). GPUs are all about parallel execution and if you would throw a branch in there it, the GPU won't be very happy.

For the most part, the same is true for CPUs but on a lesser extent.

In the book "Masters of Doom" John Romero, the game designer, argued with John Carmack on multiple occasions to add sliding walls so they could add secerts in the levels for players to find. However, John Carmack refused multiple times because that would create branches and slow down the program, noticeably since back then, Wolfenstein 3D required an intel 286 as a minimum spec or an intel 386 as a recommended spec. The game needed to run fast, and branches would really hurt performance back then on those CPUs.

In conclusion, Cyclomatic complexity is important to ensure the code is not complex and, therefore, would make it run fast.

Referances:

Blog Cloudflare. 2022. Branch predictor: How many "if"s are too many? Including x86 and M1 benchmarks!. [online] Available at: <https://blog.cloudflare.com/branch-predictor/> [Accessed 5 September 2022].

NVIDIA Developer. 2022. Chapter 34. GPU Flow-Control Idioms. [online] Available at: <https://developer.nvidia.com/gpugems/gpugems2/part-iv-general-purpose-computation-gpus-primer/chapter-34-gpu-flow-control-idioms> [Accessed 5 September 2022].