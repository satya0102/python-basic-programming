def valid_transform(faulty, valid):
    # Compare two 3x3 matrices (lists of 9 elements each)
    diff_count = sum(1 for i in range(9) if faulty[i] != valid[i])
    return diff_count == 1  # Only 1 difference means it's a valid transformation

def solve_seven_segment_problem():
    # Step 1: Parse the input
    # Read the 3x9 matrix for digits 0-9
    seg_map = []
    for _ in range(3):
        row = input().strip()
        seg_map.append(row)
    
    # Segments for digits 0 to 9
    valid_digits = []
    for i in range(0, 30, 3):  # Each digit is 3 columns wide
        valid_digits.append([seg_map[0][i:i+3], seg_map[1][i:i+3], seg_map[2][i:i+3]])
    
    # Read the faulty number's 3x3 matrix
    faulty = []
    for _ in range(3):
        faulty.append(input().strip())
    
    
    faulty_digits = []
    for i in range(0, len(faulty[0]), 3):  # Each digit is 3 columns wide
        faulty_digits.append([faulty[0][i:i+3], faulty[1][i:i+3], faulty[2][i:i+3]])
    
    
    total_sum = 0
    for faulty_digit in faulty_digits:
        valid_numbers = set()
        
        
        faulty_bits = ''.join(faulty_digit[0] + faulty_digit[1] + faulty_digit[2])
        
        
        for i, valid_digit in enumerate(valid_digits):
            
            valid_bits = ''.join(valid_digit[0] + valid_digit[1] + valid_digit[2])
            
            if valid_transform(faulty_bits, valid_bits):
                valid_numbers.add(i)
        
        if not valid_numbers:
            print("Invalid")
            return
        
        total_sum += sum(valid_numbers)
    
    print(total_sum)

