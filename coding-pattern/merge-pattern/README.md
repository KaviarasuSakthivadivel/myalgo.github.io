# Introduction

Two events `[s1, e1)` and `[s2, e2)` do _not_ conflict if and only if one of them starts after the other one ends: either `e1 <= s2` OR `e2 <= s1`. By De Morgan's laws, this means the events conflict when `s1 < e2` AND `s2 < e1`.

## Contents
* [1. Find all conflicting appointments](1.md)
* [Interview Questions](interview-questions.md)