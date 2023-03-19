# python3

def parallel_processing(n, m, data):
    output = []

    assigned_jobs = [(i, 0) for i in range(n)]

    
    for i in range(m):
        
        thread_index, start_time = min(assigned_jobs, key=lambda x: x[1])


        output.append((thread_index, start_time))
        assigned_jobs[thread_index] = (thread_index, start_time + data[i])

    return output


def main():
    
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    
    result = parallel_processing(n, m, data)

    
    for thread_index, start_time in result:
        print(thread_index, start_time)




if __name__ == "__main__":
    main()
