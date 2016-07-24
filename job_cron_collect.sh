#!/bin/bash
cd /home/e220314/qa_py/; ansible-playbook -i inventory qalpy.yml; ./pars_log.py
