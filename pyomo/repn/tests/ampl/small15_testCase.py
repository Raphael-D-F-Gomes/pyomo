#  ___________________________________________________________________________
#
#  Pyomo: Python Optimization Modeling Objects
#  Copyright (c) 2008-2022 National Technology and Engineering Solutions of Sandia, LLC
#  Under the terms of Contract DE-NA0003525 with National Technology and
#  Engineering Solutions of Sandia, LLC, the U.S. Government retains certain
#  rights in this software.
#  This software is distributed under the 3-clause BSD License.
#  ___________________________________________________________________________
#
# Author:  Gabe Hackebeil
# Purpose: For regression testing to ensure that the Pyomo
#          NL writer properly reports the values corresponding
#          to the nl file header line with the label
#          '# nonlinear vars in constraints, objectives, both'
#
# Test if variables in deactivated blocks are found
#

from pyomo.environ import ConcreteModel, Var, Block, Objective, Constraint

model = ConcreteModel()

model.x = Var(initialize=1.0)
model.b = Block()
model.b.y = Var(initialize=1.0)

model.OBJ = Objective(expr=model.x**2)

model.CON1 = Constraint(expr=model.b.y**2 == 4)

model.b.deactivate()

