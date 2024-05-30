---
title: Principles
layout: page
comments: false
hide_footer: true
---

_This page was last updated on April 27, 2022.__

The most recent draft can be found [here][draft]; readers are encouraged to
leave comments and suggestions, or to contact members of the P3HPC committee
via e-mail.

[draft]: https://docs.google.com/document/d/1wqOmoYlu9i4Oz6WU4yoe3SiGxgiP6Tdh_96qoM1lLCQ/edit?usp=sharing

# Motivation and Goals

The intersection of performance, portability and productivity (P3) is of broad
interest to many in the high performance computing (HPC+AI) community. We
invite submissions from a diverse group of authors hailing from a wide range of
fields – compiler, language and runtime experts; performance engineers; and
domain scientists – and it is important to reflect this diversity of experience
in the P3HPC program committee.

Such diversity brings with it some challenges; experts in different fields may
disagree on which aspects of P3 are most challenging or most important, and
there have been instances where it has been difficult to ensure consistency
across submission quality and reviewer feedback.

The goals of this document are twofold:

1. To establish the key shared principles and expectations shared by all
   members of the P3HPC community, to provide clearer guidance to authors and
   reviewers.


2. To capture the remaining sources of disagreement within the community, to
   help inform future research directions and provide helpful clarity to drive
   the community even closer to a shared vision.

# Key Principles

## Adherence to Scientific Principles

P3 practitioners should avoid vague claims like “good performance” or “higher
productivity”. To facilitate discussion and ensure forward progress, papers
should support claims with data, and justify why the selected data supports the
claim(s).

Comparisons that are both apples to apples, that use benchmarks or workloads
that are meaningfully representative, and that are made on current hardware and
software generations make a much more compelling basis for P3 claims.  This
does not exclude cross-generational studies showing the value of techniques in
creating code that is portable over time, but those studies are stronger when
using a control sample (e.g. code written for previous generation hardware run
on current generation hardware to demonstrate cross-generational portability).

## Clear Goals

P3 practitioners should state their goals clearly, to assist readers and
reviewers in evaluating it.
  
- What is the performance target (and why)? 

- Is platform-specific code acceptable to the authors and their intended
  audience, or not?  What level of expertise is considered acceptable?

- Which aspect of programmer productivity is the focus?  

While views may vary in these goals and expectations, assumptions about target
audiences should be clearly stated and supportable.

## Performance Measurements

Raw performance numbers and speed-ups provide little insight into an
application’s ability to execute across different architectures. P3
practitioners should demonstrate how their achieved performance compares to the
effective peak capabilities of each architecture, and/or to the
state-of-the-art.

Effective peak capabilities include both hardware capabilities and software
tuning.  For example, McCalpin Stream Triad is a reasonable measure of
attainable peak bandwidth that may be more meaningful than hardware peak
specifications, and effective use of available (including platform-specific)
programming models is a more meaningful measure of effective performance than
ninja coding in assembly unless it occurs in vendor libraries.

It may also be important to consider how achieved performance compares to the
state-of-the-art.  Demonstrating that an application achieves a high fraction
of effective peak is not equivalent to proving that the application is using
appropriate algorithms on each architecture.  Attention to this distinction is
particularly important for high-level abstractions.

# Sources of Disagreement

_A summary of ongoing discussion from the living draft is presented here.
For more information, readers should consult the draft._

## Definitions and Metrics

There remains some disagreement about what each of the three Ps means, and how
to measure them. Should the community strive for shared definitions and
metrics, or is it sufficient that authors provide explanations and
justifications?

## Performance Consistency

Another common disagreement is the importance of performance consistency (i.e.
spread) across architectures vs architecture utilization. How desirable is an
application that achieves the same (low) fraction of achievable peak
performance across multiple architectures, or which runs at the same speed
everywhere but does not run “fast enough” to be useful?

## Algorithmic Efficiency

Discussions of performance typically focus on quantifying performance
measurements (e.g. percent of peak), and ignore the inherent efficiency of an
algorithm.  Is the code doing the minimum number of arithmetic operations, or
the minimum number of loads/stores?  Is it efficiently parallelized? How much
extra work/memory do we incur by threading? How much extra do we pay for
synchronization?

## Workload Scaling

An often overlooked component of performance portability is a code's ability to
make use of available parallelism.  Different architectures can have wildly
different amounts of parallelism that need to be utilized, leading to very
different efficient workloads on different platforms.  Smaller, lower
dimensional workloads may run at peak efficiency on CPU architectures, but are
completely incapable of running efficiently on GPU architectures.  Does that
mean the code isn’t portable? Since available parallelism is tied to problem
size, how do strong- and weak-scaling fit into the notion of a code’s
performance and portability?

## Measuring Productivity

"Productivity” is arguably the hardest P to define and measure. It could mean
fewer lines of code, less time to develop a new algorithm, less time to port
existing code to another architecture, less time to maintain, and/or less time
to onboard a new developer. Are these definitions compatible, and what are the
trade-offs? If a code is highly portable and compact (in lines of code) but is
extremely complex, is that better than a code that is less portable but easier
to debug and maintain?
