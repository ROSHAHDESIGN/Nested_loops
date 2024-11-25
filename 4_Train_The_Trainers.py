#broyat na jurito
number_judges = int(input())

total_sum = 0
presentation_count = 0
#sled tova na OTDELEN RED se chete imeto na presentaciyata
command = input()
#LOOP koito vyrti do command "Finish"
while command != "Finish":
    current_presentation = command

    presentation_count += 1

    current_scores = 0
    #vytreshen loop za vsqka edna presentacia, range(broyat na jurito)
    for j in range(number_judges):
        #na NOV red se chetat n-broy ocenki
        judge_score = float(input())
        #kato se izvyrti FOR-a tekushtite tochki shte se uvelichavat,s poluchenite novi
        current_scores += judge_score

    average_score_each_pres =(current_scores)/number_judges
    print(f"{current_presentation} - {average_score_each_pres:.2f}.")

    total_sum += current_scores

    command = input()

total_average_score = total_sum / (number_judges * presentation_count)
print(f"Student's final assessment is {total_average_score:.2f}.")