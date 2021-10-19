def print_iterations(iterations):
    """
    This will display the iterations in tabular form on the console
    """
    print("k\t\tx1\t\t\tx2\t\t\tx3\t\t\tx4\t\t\tx5\t\t\tx6")
    for i in range(0, len(iterations)):
        print(f"{i}\t", end=' ')
        for j in range(len(iterations[i])):
            # set the output precision to 4 decimal places only
            ans = "{:.4f}".format(iterations[i][f'x{j + 1}'])
            if iterations[i][f'x{j + 1}'] < 0: print(f"{ans}\t", end=' ')
            else: print(f"{ans}\t\t", end=' ')
        print()


def jacobi(equations, k):
    # equations gets an array of equations
    # k gets the number of iterations required
    # returns a list of iterations of size k
    iterations = [{f"x{i+1}": 0 for i in range(len(equations))}]
    for i in range(1, k+2):
        # create a dictionary which will store the values of current iteration
        # append it to the list of dictionaries
        iterations.append({f"x{i+1}": 0 for i in range(len(equations))})
        for j in range(len(equations)):
            # evaluate each equation using the values from previous iteration
            iterations[i][f"x{j+1}"] = equations[j].evaluate(iterations[i-1])
    iterations.remove({f"x{i+1}": 0 for i in range(len(equations))}) # remove the first empty iteration
    return iterations


def siedel(equations, k):
    # equations gets an array of equations
    # k gets the number of iterations required
    # returns a list of iterations of size k
    iterations = [{f"x{i+1}": 0 for i in range(len(equations))}]
    for i in range(0, k):
        for j in range(len(equations)):
            # evaluate each equation using the values from current iteration
            iterations[i][f"x{j+1}"] = equations[j].evaluate(iterations[i])
        # create a new dictionary to allocate new memory location for current iteration
        curr_iteration = {f"x{j+1}": iterations[i][f"x{j+1}"] for j in range(len(equations))}
        # append it to the list of dictionaries
        iterations.append(curr_iteration)
    return iterations
