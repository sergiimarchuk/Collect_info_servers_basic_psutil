#!/bin/bash
cd /home/USERNAMEHOMEFOLDER/qa_py/; ansible-playbook -i inventory qalpy.yml; ./pars_log.py
