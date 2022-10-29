from pyparsing import (
    Word,
    delimitedList,
    Optional,
    Group,
    alphas,
    alphanums,
    Forward,
    oneOf,
    quotedString,
    infixNotation,
    opAssoc,
    restOfLine,
    CaselessKeyword,
    ParserElement,
    pyparsing_common as ppc,
)


def operatorOperands(tokenlist):
    "generator to extract operators and operands in pairs"
    it = iter(tokenlist)
    while 1:
        try:
            yield next(it), next(it)
        except StopIteration:
            break


class EvalConstant:
    "Class to evaluate a parsed constant or variable"
    vars_ = {}

    def __init__(self, tokens):
        self.value = tokens[0]

    def eval(self):
        if self.value in EvalConstant.vars_:
            return EvalConstant.vars_[self.value]
        else:
            try:
                return int(self.value)
            except Exception as exc:
                return float(self.value)


class EvalComparisonOp:
    "Class to evaluate comparison expressions"
    opMap = {
        "<": lambda a, b: a < b,
        "<=": lambda a, b: a <= b,
        ">": lambda a, b: a > b,
        ">=": lambda a, b: a >= b,
        "!=": lambda a, b: a != b,
        "=": lambda a, b: a == b,
        "==": lambda a, b: a == b,
        "<>": lambda a, b: a != b,
    }

    def __init__(self, tokens):
        self.value = tokens

    def eval(self):
        val1 = self.value[0].eval()
        for op, val in operatorOperands(self.value[1:]):
            fn = EvalComparisonOp.opMap[op]
            val2 = val.eval()
            if not fn(val1, val2):
                break
            val1 = val2
        else:
            return True
        return False


class EvalLogical:
    "Class to evaluate logical expressions"
    opMap = {
        "and": lambda a, b: a and b,
        "or": lambda a, b: a or b,
        "not": lambda a: not a
    }

    def __init__(self, tokens):
        self.value = tokens[0]

    def eval(self):
        val = self.value[0]
        val1 = val.eval()
        for op, val in operatorOperands(self.value[1:]):
            fn = EvalLogical.opMap[op]
            val2 = val.eval()
            if not fn(val1, val2):
                break
            val1 = val2
        else:
            return True
        return False


class EvalInCondition:
    def __init__(self, tokens):
        self.lvalue = tokens[0]
        self.op = tokens[1]
        self.rvalue = tokens[2]

    def eval(self):
        val1 = self.lvalue.eval()
        vals = self.rvalue.eval()
        result = val1 in vals
        return result


class EvalValuesList:
    def __init__(self, tokens):
        self.lbracket = tokens[0]
        self.values = tokens[1:-1]
        self.rbracket = tokens[-1]

    def eval(self):
        vals = set()
        for val in self.values:
            v = val.eval()
            vals.add(v)
        return vals


def main():
    # define the grammar
    whereStmt = Forward()

    AND, OR, IN, IS, NOT, NULL = map(
        CaselessKeyword, "and or in is not null".split()
    )
    NOT_NULL = NOT + NULL

    ident = Word(alphas, alphanums + "_$").setName("identifier")
    columnName = delimitedList(ident, ".", combine=True).setName("column name")
    columnName.addParseAction(ppc.upcaseTokens)
    columnName.addParseAction(EvalConstant)

    # columnNameList = Group(delimitedList(columnName).setName("column_list"))

    binop = oneOf("= == != < > >= <=", caseless=True).setName("binop")
    realNum = ppc.real().setName("real number")
    intNum = ppc.signed_integer()

    columnRval = (
            realNum | intNum | quotedString | columnName
    ).setName("column_rvalue")  # need to add support for alg expressions

    columnRval.setParseAction(EvalConstant)

    valuesList = ("(" + delimitedList(columnRval).setName("in_values_list") + ")")
    valuesList.setParseAction(EvalValuesList)

    inCondition = (columnName + IN + valuesList).setName("in_condition")
    inCondition.setParseAction(EvalInCondition)

    commonCondition = (columnName + binop + columnRval).setName("common_condition")
    commonCondition.setParseAction(EvalComparisonOp)

    whereCondition = (commonCondition | inCondition).setName("where_condition")
        # | (columnName + IN + Group("(" + whereStmt + ")"))
        # | (columnName + IS + (NULL | NOT_NULL))
    # ).setName("where_condition")

    # whereCondition.setParseAction(EvalComparisonOp)

    whereExpression = infixNotation(
        whereCondition,
        [
            (NOT, 1, opAssoc.RIGHT),
            (AND, 2, opAssoc.LEFT),
            (OR, 2, opAssoc.LEFT),
        ],
    ).setName("where_expression")

    whereExpression.setParseAction(EvalLogical)

    # whereStmt <<= (Group(whereExpression)).setName("where_statement")
    whereStmt <<= whereExpression

    # whereStmt.runTests(queries)

    queries = [
               "Age > 30 and Salary < 100000",
               "Age > 30 and Salary in (100000, 1, 0)",
               "Age > 30 and Salary < (100000 + 1)",
               ]

    EvalConstant.vars_["AGE"] = 90
    EvalConstant.vars_["SALARY"] = 55000

    for q in queries:
        print(f"Statement - {q}")
        # whereStmt.set_debug(True)
        result = whereStmt.parseString(q)
        print(f"Result - {result[0].eval()}")


if __name__ == "__main__":
    main()
