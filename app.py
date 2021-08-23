import math

class SineTheorem:
    def resolve(self, a = None, b = None, c = None, A = None, B = None, C = None):
        self.a, self.b, self.c = a, b, c
        self.A, self.B, self.C = A, B, C
        self.sides = ["a", "b", "c"]
        self.angles = ["A", "B", "C"]

        vars = { "a":self.a, "b":self.b, "c":self.c, "A":self.A, "B":self.B, "C":self.C }
        self.goodVars = dict()
        for var in vars:
            if not vars[var] == None:
                self.goodVars[var] = vars[var]
        self.findCase()
        print(self.goodVars)

    def findCase(self):
        numSides = int()  
        for x in self.sides:
            if x in self.goodVars:
                numSides += 1

        if numSides == 1:
            self.firstCaseSen()
        elif numSides == 2:
            self.secondCaseSen()
        elif numSides == 3:
            self.firstCaseCos()

    def firstCaseCos(self):
        a = self.goodVars["a"]
        b = self.goodVars["b"]
        c = self.goodVars["c"]
        process = list()
        solutions.write(f'cos(A) = ({b})² + ({c})² - ({a})² / 2 * {b} * {c}\n')
        process.append(round((b**2) + (c**2) - (a**2), 3))
        solutions.write(f'cos(A) = {process[0]} / 2 * {b} * {c}\n')
        process.append(round(2 * b * c, 3))
        solutions.write(f'cos(A) = {process[0]} / {process[1]}\n')
        process.append(round(process[0] / process[1], 3))
        solutions.write(f'A = cos⁻¹({process[2]})\n')
        process.append(round(math.acos(process[2]) * 180.0 / math.pi, 3))
        solutions.write(f'A = {process[3]}\n\n')
        self.goodVars["A"] = process[3]
        self.goodVars["B"] = self.findAngle(side1=a, angle1=self.goodVars["A"], side2=b, unknown="B")
        self.findAngle2()

    def secondCaseCos(self, goodAngle):
        for angle in self.angles:
            if not angle in self.goodVars:
                badAngle = angle
                break 
        ady = list()
        unknown = goodAngle.lower()
        goodAngle = self.goodVars[goodAngle]
        radianGoodAngle = ( goodAngle * math.pi ) / 180
        process = list()
        for side in self.sides:
            if side != unknown:
                ady.append(self.goodVars[side])
        solutions.write(f'{unknown}² = {ady[0]}² + {ady[1]}² - 2({ady[0]}) * {ady[1]} * cos({goodAngle})\n')
        process.append(round(ady[0]**2 + ady[1]**2, 3))
        process.append(2 * ady[0] * ady[1])
        process.append(round(math.cos(radianGoodAngle), 3))
        solutions.write(f'{unknown}² = {process[0]} - {process[1]} * {process[2]}\n')
        process.append(round(process[0] - process[1] * process[2], 3))
        solutions.write(f'{unknown} = √({process[3]})\n')
        process.append(round(math.sqrt(process[3]), 3))
        solutions.write(f'{unknown} = {process[4]}\n\n')
        self.goodVars[unknown] = process[4]
        self.goodVars[badAngle] = self.findAngle(side1=process[4], angle1=goodAngle, side2=ady[0], unknown=badAngle)
        self.findAngle2()

        

    def firstCaseSen(self):
        self.findAngle2()
        for angle in self.angles:
            if angle.lower() in self.goodVars:
                goodSide = angle.lower()
                break
        
        for angle in self.angles:
            if not angle.lower() in self.goodVars:
                self.goodVars[angle.lower()] = self.findSide(side1=self.goodVars[goodSide], angle1=self.goodVars[goodSide.upper()], angle2=self.goodVars[angle], unknown=angle.lower())                

    def secondCaseSen(self):
        for angle in self.angles:
            if angle in self.goodVars:
                goodAngle = angle
        try:
            for angle in self.angles:
                if not angle in self.goodVars and angle.lower() in self.goodVars:
                    self.goodVars[angle] = self.findAngle(side1=self.goodVars[goodAngle.lower()], angle1=self.goodVars[goodAngle], side2=self.goodVars[angle.lower()], unknown=angle)
                    break
    
            badSide = self.findAngle2().lower()
            self.findSide(side1=self.goodVars[goodAngle.lower()], angle1=self.goodVars[goodAngle], angle2=self.goodVars[badSide.upper()], unknown=badSide)
        except:
            self.secondCaseCos(goodAngle)

    def findSide(self, side1, angle1, angle2, unknown):
        radianAngle1 = ( angle1 * math.pi ) / 180
        radianAngle2 = ( angle2 * math.pi ) / 180
        process = list()
        solutions.write(f'{side1} / sen({angle1}) = {unknown} / sen({angle2})\n')
        process.append(round(side1 / math.sin(radianAngle1), 3))
        solutions.write(f'{process[0]} = {unknown} / sen({angle2})\n')
        solutions.write(f'{process[0]} * sen({angle2}) = {unknown}\n')
        process.append(round(process[0] * math.sin(radianAngle2), 3))
        solutions.write(f'{process[1]} = {unknown}\n\n')
        return process[1]

    def findAngle(self, side1, angle1, side2, unknown):
        radianAngle1 = ( angle1 * math.pi ) / 180
        process = list()
        solutions.write(f'{side1} / sen({angle1}) = {side2} / sen({unknown})\n')
        process.append(round(side1 / math.sin(radianAngle1), 3))
        solutions.write(f'{process[0]} = {side2} / sen({unknown})\n')
        solutions.write(f'sen({unknown}) = {side2} / {process[0]}\n')
        process.append(round(side2 / process[0],3))
        solutions.write(f'{unknown} = sen⁻¹({process[1]})\n')
        process.append(round(math.asin(process[1]) * 180 / math.pi, 3))
        solutions.write(f'{unknown} = {process[2]}\n\n')
        return process[2]

    def findAngle2(self):
        goodAngles = list()
        for angle in self.angles:
            if not angle in self.goodVars:
                badAngle = angle
                continue
            goodAngles.append(angle)

        solutions.write(f'{badAngle} = 180° - ({self.goodVars[goodAngles[0]]} + {self.goodVars[goodAngles[1]]})\n')
        self.goodVars[badAngle] = round(180 - (self.goodVars[goodAngles[0]] + self.goodVars[goodAngles[1]]), 3)
        solutions.write(f'{badAngle} = {self.goodVars[badAngle]}\n\n')
        return badAngle

problems = open ('problems.txt','r')
numProblem = 1
solutions = open("solutions.txt", "w")
sineTheorem = SineTheorem()
for problem in problems:
    args = dict()
    vars = problem.split()
    for var in range(len(vars)):
        args[vars[var][0]] = float(vars[var][2:])
    solutions.write(f'Ejercicio numero {numProblem}\n')
    solutions.write(f'\n{problem}\n\n')
    try:
        sineTheorem.resolve(**args)
    except:
        solutions.write(f"\nEl problema dado esta mal formulado, matematicamente.\n\n")
    numProblem += 1