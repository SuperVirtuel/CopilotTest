from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum
from typing import Union


class OperationType(Enum):
    """Enum for calculator operation types"""
    ADD = "addition"
    SUBTRACT = "subtraction"
    MULTIPLY = "multiplication"
    DIVIDE = "division"


@dataclass
class CalculationResult:
    """Dataclass to store calculation results"""
    operation: OperationType
    operand1: float
    operand2: float
    result: Union[float, str]
    success: bool

    def __str__(self):
        if self.success:
            return f"{self.operand1} {self._get_symbol()} {self.operand2} = {self.result}"
        return f"{self.operand1} {self._get_symbol()} {self.operand2}: {self.result}"

    def _get_symbol(self) -> str:
        symbols = {
            OperationType.ADD: "+",
            OperationType.SUBTRACT: "-",
            OperationType.MULTIPLY: "*",
            OperationType.DIVIDE: "/"
        }
        return symbols.get(self.operation, "?")


class Operation(ABC):
    """Abstract base class for calculator operations"""
    
    @abstractmethod
    def execute(self, a: float, b: float) -> CalculationResult:
        """Execute the operation on two operands"""
        pass

    @abstractmethod
    def get_operation_type(self) -> OperationType:
        """Return the type of operation"""
        pass


class AddOperation(Operation):
    """Concrete implementation of addition operation"""
    
    def execute(self, a: float, b: float) -> CalculationResult:
        result = a + b
        return CalculationResult(
            operation=self.get_operation_type(),
            operand1=a,
            operand2=b,
            result=result,
            success=True
        )
    
    def get_operation_type(self) -> OperationType:
        return OperationType.ADD


class SubtractOperation(Operation):
    """Concrete implementation of subtraction operation"""
    
    def execute(self, a: float, b: float) -> CalculationResult:
        result = a - b
        return CalculationResult(
            operation=self.get_operation_type(),
            operand1=a,
            operand2=b,
            result=result,
            success=True
        )
    
    def get_operation_type(self) -> OperationType:
        return OperationType.SUBTRACT


class MultiplyOperation(Operation):
    """Concrete implementation of multiplication operation"""
    
    def execute(self, a: float, b: float) -> CalculationResult:
        result = a * b
        return CalculationResult(
            operation=self.get_operation_type(),
            operand1=a,
            operand2=b,
            result=result,
            success=True
        )
    
    def get_operation_type(self) -> OperationType:
        return OperationType.MULTIPLY


class DivideOperation(Operation):
    """Concrete implementation of division operation"""
    
    def execute(self, a: float, b: float) -> CalculationResult:
        if b == 0:
            return CalculationResult(
                operation=self.get_operation_type(),
                operand1=a,
                operand2=b,
                result='Error: Division by zero',
                success=False
            )
        result = a / b
        return CalculationResult(
            operation=self.get_operation_type(),
            operand1=a,
            operand2=b,
            result=result,
            success=True
        )
    
    def get_operation_type(self) -> OperationType:
        return OperationType.DIVIDE


class Calculator:
    """Calculator class that uses operation objects"""
    
    def __init__(self):
        self._operations = {
            OperationType.ADD: AddOperation(),
            OperationType.SUBTRACT: SubtractOperation(),
            OperationType.MULTIPLY: MultiplyOperation(),
            OperationType.DIVIDE: DivideOperation()
        }
    
    def calculate(self, operation_type: OperationType, a: float, b: float) -> CalculationResult:
        """Perform a calculation using the specified operation type"""
        operation = self._operations.get(operation_type)
        if operation:
            return operation.execute(a, b)
        raise ValueError(f"Unsupported operation: {operation_type}")


if __name__ == '__main__':
    calc = Calculator()
    
    # Perform various calculations
    results = [
        calc.calculate(OperationType.ADD, 5, 3),
        calc.calculate(OperationType.SUBTRACT, 5, 3),
        calc.calculate(OperationType.MULTIPLY, 5, 3),
        calc.calculate(OperationType.DIVIDE, 6, 3),
        calc.calculate(OperationType.DIVIDE, 6, 0)  # Test division by zero
    ]
    
    # Print all results
    for result in results:
        print(result)