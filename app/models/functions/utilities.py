import os
import datetime


def define_similarity(distance):
    if distance > float(os.getenv('MIN_CONFIDENCE')):
        return {'alarm': False,
                'similarity': distance / 100}
    else:
        return {'alarm': True,
                'similarity': distance / 100}


def authResponse(id_results, biometric_results, test_results):
    return {'id_img_detection': str(id_results),
            'id_registro': biometric_results['id'],
            'id_reg_similarity': biometric_results['similarity'],
            'test_similarity': test_results['similarity'],
            'reg_alarm': biometric_results['alarm'],
            'exam_alarm': test_results['alarm']}


def getDate(offset=0):
    now = datetime.datetime.now()
    date = str(now.year) + '-' + str(now.month) + '-' + str(now.day) + '-' + \
           str(int(now.hour) + offset) + '-' + str(now.minute) + '-' + str(now.second)

    sqldate = str(now.year) + '-' + str(now.month) + '-' + str(now.day) + ' ' + \
              str(int(now.hour) + offset) + ':' + str(now.minute) + ':' + str(now.second)
    return date, sqldate
