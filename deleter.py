#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 17:59:18 2023

@author: manuelgutierrez
"""

from owlready2 import *
import pandas as pd

template_ontology = get_ontology('data_project.owl').load()

# Loop over all classes in the ontology
for instance in template_ontology.individuals():
    # Loop over the instances of the class and delete them
    destroy_entity(instance)

template_ontology.save(file="data_project.owl")