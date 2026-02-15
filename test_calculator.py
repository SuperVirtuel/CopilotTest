import unittest
from calculator import (
    Calculator,
    OperationType,
    CalculationResult,
    AddOperation,
    SubtractOperation,
    MultiplyOperation,
    DivideOperation
)


class TestOperationType(unittest.TestCase):
    """Test cases for OperationType enum"""
    
    def test_enum_values(self):
        """Test that all operation types are defined"""
        self.assertEqual(OperationType.ADD.value, "addition")
        self.assertEqual(OperationType.SUBTRACT.value, "subtraction")
        self.assertEqual(OperationType.MULTIPLY.value, "multiplication")
        self.assertEqual(OperationType.DIVIDE.value, "division")


class TestCalculationResult(unittest.TestCase):
    """Test cases for CalculationResult dataclass"""
    
    def test_successful_result_str(self):
        """Test string representation of successful calculation"""
        result = CalculationResult(
            operation=OperationType.ADD,
            operand1=5,
            operand2=3,
            result=8,
            success=True
        )
        self.assertEqual(str(result), "5 + 3 = 8")
    
    def test_failed_result_str(self):
        """Test string representation of failed calculation"""
        result = CalculationResult(
            operation=OperationType.DIVIDE,
            operand1=5,
            operand2=0,
            result="Error: Division by zero",
            success=False
        )
        self.assertEqual(str(result), "5 / 0: Error: Division by zero")
    
    def test_dataclass_fields(self):
        """Test that dataclass has all required fields"""
        result = CalculationResult(
            operation=OperationType.MULTIPLY,
            operand1=2.5,
            operand2=4.0,
            result=10.0,
            success=True
        )
        self.assertEqual(result.operation, OperationType.MULTIPLY)
        self.assertEqual(result.operand1, 2.5)
        self.assertEqual(result.operand2, 4.0)
        self.assertEqual(result.result, 10.0)
        self.assertTrue(result.success)


class TestAddOperation(unittest.TestCase):
    """Test cases for AddOperation"""
    
    def setUp(self):
        self.operation = AddOperation()
    
    def test_add_positive_numbers(self):
        """Test addition of positive numbers"""
        result = self.operation.execute(5, 3)
        self.assertEqual(result.result, 8)
        self.assertTrue(result.success)
        self.assertEqual(result.operation, OperationType.ADD)
    
    def test_add_negative_numbers(self):
        """Test addition of negative numbers"""
        result = self.operation.execute(-5, -3)
        self.assertEqual(result.result, -8)
        self.assertTrue(result.success)
    
    def test_add_mixed_numbers(self):
        """Test addition of mixed positive and negative numbers"""
        result = self.operation.execute(5, -3)
        self.assertEqual(result.result, 2)
        self.assertTrue(result.success)
    
    def test_add_floats(self):
        """Test addition of floating point numbers"""
        result = self.operation.execute(2.5, 3.7)
        self.assertAlmostEqual(result.result, 6.2, places=1)
        self.assertTrue(result.success)
    
    def test_get_operation_type(self):
        """Test that operation type is correctly returned"""
        self.assertEqual(self.operation.get_operation_type(), OperationType.ADD)


class TestSubtractOperation(unittest.TestCase):
    """Test cases for SubtractOperation"""
    
    def setUp(self):
        self.operation = SubtractOperation()
    
    def test_subtract_positive_numbers(self):
        """Test subtraction of positive numbers"""
        result = self.operation.execute(5, 3)
        self.assertEqual(result.result, 2)
        self.assertTrue(result.success)
        self.assertEqual(result.operation, OperationType.SUBTRACT)
    
    def test_subtract_negative_numbers(self):
        """Test subtraction of negative numbers"""
        result = self.operation.execute(-5, -3)
        self.assertEqual(result.result, -2)
        self.assertTrue(result.success)
    
    def test_subtract_larger_from_smaller(self):
        """Test subtraction resulting in negative"""
        result = self.operation.execute(3, 5)
        self.assertEqual(result.result, -2)
        self.assertTrue(result.success)
    
    def test_subtract_floats(self):
        """Test subtraction of floating point numbers"""
        result = self.operation.execute(5.5, 2.3)
        self.assertAlmostEqual(result.result, 3.2, places=1)
        self.assertTrue(result.success)
    
    def test_get_operation_type(self):
        """Test that operation type is correctly returned"""
        self.assertEqual(self.operation.get_operation_type(), OperationType.SUBTRACT)


class TestMultiplyOperation(unittest.TestCase):
    """Test cases for MultiplyOperation"""
    
    def setUp(self):
        self.operation = MultiplyOperation()
    
    def test_multiply_positive_numbers(self):
        """Test multiplication of positive numbers"""
        result = self.operation.execute(5, 3)
        self.assertEqual(result.result, 15)
        self.assertTrue(result.success)
        self.assertEqual(result.operation, OperationType.MULTIPLY)
    
    def test_multiply_negative_numbers(self):
        """Test multiplication of negative numbers"""
        result = self.operation.execute(-5, -3)
        self.assertEqual(result.result, 15)
        self.assertTrue(result.success)
    
    def test_multiply_by_zero(self):
        """Test multiplication by zero"""
        result = self.operation.execute(5, 0)
        self.assertEqual(result.result, 0)
        self.assertTrue(result.success)
    
    def test_multiply_floats(self):
        """Test multiplication of floating point numbers"""
        result = self.operation.execute(2.5, 4.0)
        self.assertEqual(result.result, 10.0)
        self.assertTrue(result.success)
    
    def test_get_operation_type(self):
        """Test that operation type is correctly returned"""
        self.assertEqual(self.operation.get_operation_type(), OperationType.MULTIPLY)


class TestDivideOperation(unittest.TestCase):
    """Test cases for DivideOperation"""
    
    def setUp(self):
        self.operation = DivideOperation()
    
    def test_divide_positive_numbers(self):
        """Test division of positive numbers"""
        result = self.operation.execute(6, 3)
        self.assertEqual(result.result, 2.0)
        self.assertTrue(result.success)
        self.assertEqual(result.operation, OperationType.DIVIDE)
    
    def test_divide_negative_numbers(self):
        """Test division of negative numbers"""
        result = self.operation.execute(-6, -3)
        self.assertEqual(result.result, 2.0)
        self.assertTrue(result.success)
    
    def test_divide_by_zero(self):
        """Test division by zero returns error"""
        result = self.operation.execute(5, 0)
        self.assertEqual(result.result, "Error: Division by zero")
        self.assertFalse(result.success)
    
    def test_divide_zero_by_number(self):
        """Test zero divided by number"""
        result = self.operation.execute(0, 5)
        self.assertEqual(result.result, 0.0)
        self.assertTrue(result.success)
    
    def test_divide_floats(self):
        """Test division of floating point numbers"""
        result = self.operation.execute(7.5, 2.5)
        self.assertEqual(result.result, 3.0)
        self.assertTrue(result.success)
    
    def test_get_operation_type(self):
        """Test that operation type is correctly returned"""
        self.assertEqual(self.operation.get_operation_type(), OperationType.DIVIDE)


class TestCalculator(unittest.TestCase):
    """Test cases for Calculator class"""
    
    def setUp(self):
        self.calculator = Calculator()
    
    def test_calculate_add(self):
        """Test calculator addition"""
        result = self.calculator.calculate(OperationType.ADD, 10, 5)
        self.assertEqual(result.result, 15)
        self.assertTrue(result.success)
    
    def test_calculate_subtract(self):
        """Test calculator subtraction"""
        result = self.calculator.calculate(OperationType.SUBTRACT, 10, 5)
        self.assertEqual(result.result, 5)
        self.assertTrue(result.success)
    
    def test_calculate_multiply(self):
        """Test calculator multiplication"""
        result = self.calculator.calculate(OperationType.MULTIPLY, 10, 5)
        self.assertEqual(result.result, 50)
        self.assertTrue(result.success)
    
    def test_calculate_divide(self):
        """Test calculator division"""
        result = self.calculator.calculate(OperationType.DIVIDE, 10, 5)
        self.assertEqual(result.result, 2.0)
        self.assertTrue(result.success)
    
    def test_calculate_divide_by_zero(self):
        """Test calculator handles division by zero"""
        result = self.calculator.calculate(OperationType.DIVIDE, 10, 0)
        self.assertFalse(result.success)
        self.assertIn("Division by zero", result.result)
    
    def test_all_operations_registered(self):
        """Test that all operation types are available"""
        for op_type in OperationType:
            result = self.calculator.calculate(op_type, 6, 2)
            self.assertIsInstance(result, CalculationResult)


if __name__ == '__main__':
    unittest.main()
