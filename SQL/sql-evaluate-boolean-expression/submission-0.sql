SELECT
    e.left_operand,
    e.operator,
    e.right_operand,
    case when e.operator = '>' and v1.value > v2.value then 'true'
      when e.operator = '<' and v1.value < v2.value then 'true'
      when e.operator = '=' and v1.value=v2.value then 'true'
      else 'false'
      END as value
FROM expressions e
JOIN variables v1 
    ON e.left_operand = v1.name
JOIN variables v2
    ON e.right_operand = v2.name;




