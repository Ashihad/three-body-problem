#!/bin/bash

doxygen Doxyfile
cd docs/latex/ && make 
cd ../.. && open docs/latex/refman.pdf