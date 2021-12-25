songs = ["My Heart", "Her Brain", "The Light", "A Shadow", "One Dance",
       "Two monkeys", "Happy Jumping"]
playlist = []
playlist.append(songs[0])
playlist.append(songs[2])
playlist.append(songs[4])
playlist[2] = "One Dance - Together"
playlist.pop(1)
print(playlist)

print("Don't try to memorize this")
sum_of_pi_digits=0
pi_digits = [3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3,3,8,3,2,7,9,5
             ,0,2,8,8,4,1,9,7,1,6,9,3,9,9,3,7,5,1,0,5,8,2,0,9,7,4,9,4,4,5,9
              ,2,3,0,7,8,1,6,4,0,6,2,8,2,6,2,0,8,9,9,8,6,2,8,0,3,4,8,2,5,3,4
              ,2,1,1,7,0,6,7]
print("pi digits= ", len(pi_digits))
print("times that 6 appears: ",  pi_digits.count(6))
for i in range(len(pi_digits)):
       sum_of_pi_digits+=i
print("sumatory of digits:", sum_of_pi_digits)


