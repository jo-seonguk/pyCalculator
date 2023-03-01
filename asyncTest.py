import time
import asyncio

async def coroutine_func(num):
    for i in range(1,num+1):
        print(f'{i}번!')
        await asyncio.sleep(1)
    print(f'총원 {num}명 번호 끝! 이상 무!')

async def start_coroutine():
    await asyncio.gather(
        coroutine_func(3),
        coroutine_func(2),
        coroutine_func(1)
    )
asyncio.run(start_coroutine())

async def find_users_async(n):
    for i in range(1, n + 1):
        print(f'{n}명 중 {i}번 째 사용자 조회 중 ...')
        await asyncio.sleep(1)
    print(f'> 총 {n} 명 사용자 비동기 조회 완료!')

async def process_async():
    await asyncio.gather(
        find_users_async(3),
        find_users_async(2),
        find_users_async(1),
    )

async def sleep():  
    await asyncio.sleep(1)


async def sum(name, numbers):
    total = 0
    for number in numbers:
        await sleep()
        total += number
        print(f'작업중={name}, number={number}, total={total}')
    return total

async def download_page(url) : 
    # asyncio.sleep(1)
    await asyncio.sleep(1)
    #html 분석
    print("complete download:", url)

async def main():

    task1 = asyncio.create_task(sum("A", [1, 2, 3, 4]))
    task2 = asyncio.create_task(sum("B", [1, 2, 3]))

    await task1
    await task2

    result1 = task1.result()
    result2 = task2.result()

    await download_page("url_1")
    await download_page("url_2")
    await download_page("url_3")
    await download_page("url_4")
    await download_page("url_5")
    

if __name__ == "__main__":
    start = time.time()
    asyncio.run(process_async())
    asyncio.run(main())
    end = time.time()
    print(f'>>> 비동기 처리 총 소요 시간: {end - start}')
