# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 22:19:11 2016

@author: Rodger
"""

import json
import yaml
import time

data = \
{ \
	'Header': \
    { \
        'Project Name': 'ProjectName', \
        'Date': time.strftime("%d/%m/%Y"), \
        'Time': time.strftime("%H:%M:%S"), \
		'Physics': 'Electromagnetics', \
		'Solver Type': ['Forward','DE','Transient-Explicit','FD'], \
		'Coordinate System': 'Cartesian', \
		'Unit': \
		{ \
            'Length': 'meter', \
            'Time': 'second', \
            'Frequency': 'hertz' \
		} \
    }, \
                
    'Simulation': \
	{ \
        'Time Control': \
		{ \
			'Time Window': 100e-9, \
            'Time Step': 1e-12 \
		}, \
		'Initial Condition': \
		{ \
			'Initial Values': 'C:\Test\IC.init', \
		}, \
	},\
	
	'Data Set': \
	{ \
        'Geometry Data': "C:/Test/geo.stl", \
        'Material': \
		{\
			'Air':\
			{\
				'Relative Permitivitty': \
				{\
					'Constant': 1 \
				}, \
                'Relative Permeability': \
				{\
					'Constant': 1 \
				}, \
                'Conductivity': \
				{ \
					'Constant': 0 \
				} \
			},\
			'FR4':\
			{\
				'Relative Permitivitty': \
				{\
					'Dispersion': 'C:\eps_r_dispersion.txt' \
				}, \
                'Relative Permeability': \
				{\
					'Constant': 1 \
				}, \
                'Conductivity': \
				{ \
					'Constant': 0.001 \
				} \
			},\
			'PEC':\
			{\
				'Relative Permitivitty': \
				{\
					'Dispersion': 1 \
				}, \
                'Relative Permeability': \
				{\
					'Constant': 1 \
				}, \
                'Conductivity': \
				{ \
					'Constant': 1e30 \
				} \
			},\
		},\
		'Circuit': \
		{\
			'Port1': 
			[\
				'R 0 1 50Ohm',\
				'P1 0 1' \
			]\
		},\
	},\
       
    'Physics Entities': \
	{\
        'Background': \
		{\
			'OprType': 'Interface',\
			'GeoType': 'Volume', \
            'PhyType': 'Material',\
			'DataLink': 'Air',\
			'Ranking': 1\
        },\
		'Substrate': \
		{\
			'OprType': 'Interface',\
			'GeoType': 'Volume', \
            'PhyType': 'Material',\
			'DataLink': 'FR4',\
			'Ranking': 2\
        },\
		'Trace1': \
		{\
			'OprType': 'Interface',\
			'GeoType': 'Surface', \
            'PhyType': 'Material',\
			'DataLink': 'PEC',\
			'Ranking': 10000\
        },\
		'Ground': \
		{\
			'OprType': 'Interface',\
			'GeoType': 'Surface', \
            'PhyType': 'Material',\
			'DataLink': 'PEC',\
			'Ranking': 10000\
        },\
		'LP1': \
		{\
			'OprType': 'Interface',\
			'GeoType': 'Line', \
            'PhyType': 'Circuit',\
			'DataLink': 'Port1',\
			'Ranking': 20000\
        },\
		'LP2': \
		{\
			'OprType': 'Interface',\
			'GeoType': 'Surface', \
            'PhyType': 'Circuit',\
			'DataLink': 'Port1',\
			'Ranking': 20000\
        },\
	}\
}

with open('data.json', 'w') as outfile:
    json.dump(data, outfile, indent=4, sort_keys=True, separators=(',', ':'))
    
with open('data.yaml', 'w') as outfile:
    yaml.dump(data, outfile)
    
