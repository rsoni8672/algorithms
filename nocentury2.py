# Do not use modules that are not in the standard library
import sys

def read_scores(infile):
    '''Read `country: score` pairs from infile and return a list of pairs

    Stop when `infile` reaches EOF
    '''
    scores = []
    for line in infile:
        line = line.strip()
        if line:
            country, score = line.split(':')
            scores.append([country.strip(), int(score)])

    return scores


def no_century_country_count(scores):
    no_century_count = 0
    for i in range(len(scores)):
        country, score = scores[i]
        if not country:
            # This country was already processed earlier
            continue
        
        centuries = 0
        for j in range(i+1, len(scores)):
            country1, score1 = scores[j]
            if country == country1:
                if score1 >= 100:
                    centuries += 1

                # disable checking of this same country again
                scores[j][0] = ''

        if not centuries:
            # No century has been scored against `country`
            no_century_count += 1

    return no_century_count


def run():
    scores = read_scores(sys.stdin)
    scores = [["India", 3]]
    no_century_count = no_century_country_count(scores)
    print(no_century_count)

if __name__ == '__main__':
    run()
