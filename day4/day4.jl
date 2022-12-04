"""
Task 1:

Some of the pairs have noticed that one of their assignments fully contains the other.
For example, 2-8 fully contains 3-7, and 6-6 is fully contained by 4-6.
In pairs where one assignment fully contains the other, one Elf in the pair would be
exclusively cleaning sections their partner will already be cleaning, so these seem
like the most in need of reconsideration. In this example, there are 2 such pairs.

In how many assignment pairs does one range fully contain the other?

Task 2:

In how many assignment pairs do the ranges overlap?

"""

function task1(assignments::String)
    fully_contained_counter::Int = 0
    for assignment in split(assignments, "\n")
        length(assignment) == 0 && break  # skip any blank lines
        assgn1::String, assgn2::String = split(assignment, ",")
        min1::Int, max1::Int = [parse(Int, num) for num in split(assgn1, "-")]
        min2::Int, max2::Int = [parse(Int, num) for num in split(assgn2, "-")]
        if min1 ≤ min2 && max1 ≥ max2
            fully_contained_counter += 1
        elseif min2 ≤ min1 && max2 ≥ max1
            fully_contained_counter += 1
        end
    end

    println("Task 1 output: $(fully_contained_counter)")
end


function task2(assignments::String)
    overlapping_counter::Int = 0
    for assignment in split(assignments, "\n")
        length(assignment) == 0 && break  # skip any blank lines
        assgn1::String, assgn2::String = split(assignment, ",")
        min1::Int, max1::Int = [parse(Int, num) for num in split(assgn1, "-")]
        min2::Int, max2::Int = [parse(Int, num) for num in split(assgn2, "-")]
        set1 = Set(min1:max1)
        set2 = Set(min2:max2)
        if length(intersect(set1, set2)) != 0
            overlapping_counter += 1
        end
    end

    println("Task 2 output: $(overlapping_counter)")
end


function main()
    project_dir = dirname(dirname(@__FILE__))
    input_file = joinpath(project_dir, "inputs", "day4.txt")
    filestream = open(input_file, "r")
    problem_input::String = read(filestream, String)
    close(filestream)

    task1(problem_input)
    task2(problem_input)
end


main()
