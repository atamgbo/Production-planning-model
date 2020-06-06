# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 23:41:22 2019

@author: atamg
"""

from __future__ import print_function, absolute_import, division
import sys
import os


def main(argc, argv):
    from amplpy import AMPL, DataFrame
    os.chdir(os.path.dirname(__file__) or os.curdir)
    try:
        ampl = AMPL()
        ampl.setOption('solver', 'cplexamp')
        if argc > 1:
            ampl.setOption('solver', argv[1])

        # Read the model file
        modelDirectory = argv[2] if argc == 3 else os.path.join('..', 'models')
        ampl.read(os.path.join(modelDirectory, 'Dr/pigskin_updated1.mod'))

        period0 = [0]

        df = DataFrame('ONLY0')
        df.setColumn('ONLY0', period0)
        ampl.setData(df, 'ONLY0')
        
        period0toends = [0,1]

        df = DataFrame('PERIOD0_TO_END')
        df.setColumn('PERIOD0_TO_END', period0toends)
        ampl.setData(df, 'PERIOD0_TO_END')
        
        period1toends = [1]

        df = DataFrame('PERIOD1_TO_END')
        df.setColumn('PERIOD1_TO_END', period1toends)
        ampl.setData(df, 'PERIOD1_TO_END')
        
        products = ['1P', '2P']

        df = DataFrame('PRODUCT')
        df.setColumn('PRODUCT', products)
        ampl.setData(df, 'PRODUCT')

        resources = ['1R', '2R']

        df = DataFrame('RESOURCE')
        df.setColumn('RESOURCE', resources)
        ampl.setData(df, 'RESOURCE')
        
        scenarios = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]


        df = DataFrame('SCENARIO')
        df.setColumn('SCENARIO', scenarios)
        ampl.setData(df, 'SCENARIO')
        
        
        inv0prod = [
                [0,0],
                [0,0],
                [0,0],
                [0,0],
                [0,0],
                [0,0],
                [0,0],
                [0,0],
                [0,0],
                [0,0],
                [0,0],
                [0,0],
                [0,0],
                [0,0],
                [0,0],
                [0,0],
                [0,0],
                [0,0],
                [0,0],
                [0,0],
                [0,0],
                [0,0],
                [0,0],
                [0,0],
                [0,0],
                [0,0],
                [0,0],
                [0,0],
                [0,0],
                [0,0]
                ]
        df = DataFrame(('SCENARIO','PRODUCT'),'Inv0prod')
        df.setValues({
            (scenario, product): inv0prod[s][i]
            for s, scenario in enumerate(scenarios)
            for i, product in enumerate(products)
        })
        ampl.setData(df)
        
        
        
        prodcost = [
            [12.5],
            [12.55]
        ]

        df = DataFrame(('PRODUCT', 'PERIOD1_TO_END'), 'Prodcost')
        df.setValues({
            (product, period1toend): prodcost[i][t]
            for i, product in enumerate(products)
            for t, period1toend in enumerate(period1toends)
        })
        ampl.setData(df)
        
        
        Resource = [
            [ 16,   100],
            [ 24,   200]
        ]

        df = DataFrame(('PRODUCT', 'RESOURCE'), 'Resource')
        df.setValues({
            (product, resource): Resource[i][r]
            for i, product in enumerate(products)
            for r, resource in enumerate(resources)
        })
        ampl.setData(df)
        
        avail = [
           [138516],
           [278847]
        ]

        df = DataFrame(('RESOURCE', 'PERIOD1_TO_END'), 'avail')
        df.setValues({
            (resource, period1toend): avail[r][t]
            for r, resource in enumerate(resources)
            for t, period1toend in enumerate(period1toends)
        })
        ampl.setData(df)
        
        
        perhold = [
            [0.88],
            [0.88]
        ]

        df = DataFrame(('PRODUCT', 'PERIOD1_TO_END'), 'perhold')
        df.setValues({
            (product, period1toend): perhold[i][t]
            for i, product in enumerate(products)
            for t, period1toend in enumerate(period1toends)
        })
        ampl.setData(df)
        
        prob = [
             0.03333333, 0.03333333, 0.03333333, 0.03333333, 0.03333333, 0.03333333, 0.03333333, 0.03333333, 0.03333333, 0.03333333, 0.03333333, 0.03333333, 0.03333333, 0.03333333, 0.03333333, 0.03333333, 0.03333333, 0.03333333, 0.03333333, 0.03333333, 0.03333333, 0.03333333, 0.03333333, 0.03333333, 0.03333333, 0.03333333, 0.03333333, 0.03333333, 0.03333333, 0.03333333 
        ]

        df = DataFrame(('SCENARIO'), 'prob')
        df.setValues({
            (scenario): prob[s]
            for s, scenario in enumerate(scenarios)
        })
        ampl.setData(df)
        
        MPC = [
             800
        ]

        df = DataFrame(('PERIOD1_TO_END'), 'MPC')
        df.setValues({
            (period1toend): MPC[t]
            for t, period1toend in enumerate(period1toends)
        })
        ampl.setData(df)
        
        MS = [
             100
        ]

        df = DataFrame(('PERIOD1_TO_END'), 'MS')
        df.setValues({
            (period1toend): MS[t]
            for t, period1toend in enumerate(period1toends)
        })
        ampl.setData(df)
        
        Purchase_cost = [
            [10],
            [10]
        ]

        df = DataFrame(('PRODUCT', 'PERIOD1_TO_END'), 'Purchase_cost')
        df.setValues({
            (product, period1toend): Purchase_cost[i][t]
            for i, product in enumerate(products)
            for t, period1toend in enumerate(period1toends)
        })
        ampl.setData(df)
        
       
        Demand = [
            [[216],[191 ]],[[290],[330 ]],[[224],[194 ]],[[283],[329 ]],[[159],[164 ]],[[215],[349 ]],[[247],[201 ]],[[201],[328 ]],[[343],[230 ]],[[326],[278 ]],[[319],[342 ]],[[223],[298 ]],[[292],[191 ]],[[262],[284 ]],[[285],[200 ]],[[296],[346 ]],[[210],[318 ]],[[200],[257 ]],[[314],[336 ]],[[205],[290 ]],[[174],[184 ]],[[258],[290 ]],[[284],[158 ]],[[264],[312 ]],[[228],[333 ]],[[239],[255 ]],[[190],[322 ]],[[344],[219 ]],[[280],[241 ]],[[186],[254 ]]        
        ]
        
        df = DataFrame(('SCENARIO','PERIOD1_TO_END','PRODUCT'), 'Demand')
        df.setValues({
            (scenario,period1toend,product): Demand[s][t][i-1]
            for s, scenario in enumerate(scenarios)
            for t, period1toend in enumerate(period1toends)
            for i, product in enumerate(products)
        })
        ampl.setData(df)
        
        
        ampl.solve()

        print('Objective: {}'.format(ampl.getObjective('Total_cost').value()))
        
        produce = ampl.getVariable('Produce')
        df = produce.getValues()
        # Print them
        print(df)
        # Get the values of the variable in a dataframe object
        inventory = ampl.getVariable('Inventory')
        df = inventory.getValues()
        # Print them
        print(df)
        

        
    except Exception as e:
        print(e)
        raise


if __name__ == '__main__':
    main(len(sys.argv), sys.argv)
