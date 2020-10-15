import datetime


def solution(n, customers):
    kiosk_count = [0] * n
    kiosks = [0] * n
    YEAR = 2020
    time_spent = []

    arrivals = []
    for customer in customers:
        customer = customer.split()
        M, D = map(int, customer[0].split('/'))
        HH, MM, SS = map(int, customer[1].split(':'))
        time_spent.append(int(customer[2]))

        visit = datetime.datetime(YEAR, M, D, HH, MM, SS)
        if arrivals:
            last_customer = arrivals[-1]
            delta = visit - last_customer
            delta_second = delta.total_seconds()
            if delta_second < 0:
                YEAR += 1
                
        visit = datetime.datetime(YEAR, M, D, HH, MM, SS)

            
        arrivals.append(visit)

    # print(arrivals)

    for i in range(n):
        if len(customers) > i:
            kiosks[i] = (arrivals[i] + datetime.timedelta(minutes=time_spent[i]))
            kiosk_count[i] += 1
    print(kiosks)
    
    for i in range(n, len(customers)):
        this_customer = arrivals[i]
        min_wait = -999999999
        select_kiosk = -1
        print('this', this_customer)
        for j in range(len(kiosks)):
            print(kiosks[j])
                
            time_delta = this_customer - kiosks[j]

            if time_delta.total_seconds() > min_wait:
                min_wait = time_delta.total_seconds()
                select_kiosk = j
            # print(time_delta.total_seconds())
        
        kiosk_count[select_kiosk] += 1
        kiosks[select_kiosk] = arrivals[i] + datetime.timedelta(minutes=time_spent[i])

    print(kiosk_count)       
    answer = 'Bonjour'
    return answer


n = 3
customers = ["10/01 23:20:25 30", "10/01 23:25:50 26", "10/01 23:31:00 05", "10/01 23:33:17 24",
             "10/01 23:50:25 13", "10/01 23:55:45 20", "10/01 23:59:39 03", "10/02 00:10:00 10"]
print(solution(n, customers))
