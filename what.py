def solution(histogram):
    stack = []
    i = 0
    max_area = 0

    while i < len(histogram):
        # Stack keeps track of the last largest height
        # As soon as we encounter a height smaller than the previous, calculate max area
        while stack and histogram[i] < histogram[stack[-1]]:
            top = stack.pop()
            width = i if not stack else i - stack[-1] - 1
            edge = min(width, histogram[top])
            max_area = max(max_area, edge * edge)

        stack.append(i)
        i += 1

    # Process the remaining heights in the stack
    while stack:
        top = stack.pop()
        width = i if not stack else i - stack[-1] - 1
        edge = min(width, histogram[top])
        max_area = max(max_area, edge * edge)

    return max_area

print(solution(histogram=[1,2,3,2,1]))