"""
피자를 여섯조각으로 자름
매개변수 : 나눠먹을 사람 n 명
조건 : n명이 주문한 피자 다 먹는다
출력 : 최소 몇 판을 시켜야 하는지
"""


def solution(n):

  pieces = 6 # 한 판에 피자 6조각

  for i in range(max(n,pieces), (n*pieces)+1):
    # 사람 수 n 과 피자 조각 pieces 의 최소공배수 구하기
    # 둘 중에 큰 수를 기준으로 둘을 곱한 수까지의 범위에서 구해야함
    # 둘을 곱해버리면 일단 공배수가 되버림을 인지!
    # range() 두번째 인자 미만 까지 임을 인지하고 +1 을 해주었어야함

    if i % n == 0 and i % pieces == 0:
      # i = 최소공배수. n과 pieces 둘다 나눠서 0이 되는 수를 찾아라
      answer = int(i/pieces)
      # 그 최소공배수를 구했으면 거기서 피자 조각 6 을 나누어야 몇 판이 되는지 구함

      return answer