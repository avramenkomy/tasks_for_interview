def appearance(intervals):

    lst = []
    counter = 0
    start_joint_time = 0
    joint_time = 0

    for item in intervals['data']:
        for elem in intervals['data'][item]:
            
            if intervals['data'][item].index(elem) % 2 == 0:
                lst.append((elem, 1))
            else:
                lst.append((elem, -1))

    
    lst.sort()

    for i in lst:
        counter += i[1]

        if counter == 3:
            start_joint_time = i[0]
        
        if counter == 2 and start_joint_time > 0:
            joint_time += i[0] - start_joint_time
            start_joint_time = 0
    
    return joint_time

intervals = { 'data': { 

            'lesson': [1594663200, 1594666800],
            'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
            'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
             
    'answer': 3117
}

if __name__ == "__main__":
   print(appearance({'data': {
            'lesson': [1594702800, 1594706400],
             'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
             'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    'answer': 3577
    }))
