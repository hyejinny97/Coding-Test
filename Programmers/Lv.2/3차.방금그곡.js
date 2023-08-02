// https://school.programmers.co.kr/learn/courses/30/lessons/17683
// 코딩테스트연습 < 2018 KAKAO BLIND RECRUITMENT < 문제.[3차] 방금그곡



// 입력
/*
1. 네오가 기억한 멜로디를 담은 문자열 m
- 1 <= m 길이 <= 1439
2. 방송된 곡의 정보를 담고 있는 배열 musicinfos
- 0 < musicinfos 길이 <= 100
- element = "음악이 시작한 시각,끝난 시각,음악 제목,악보 정보"
- 시각은 24시간 HH:MM 형식
- 1 <= 움악 제목 길이 <= 64
- 1 <= 악보 정보 음 길이 <= 1439
*/




// 출력
/*
1. 조건과 일치하는 음악 제목을 출력

<조건>
- 네오가 기억한 멜로디/악보에 사용된 음: C, C#, D, D#, E, F, F#, G, G#, A, A#, B (12개)
- 각 음은 1분에 1개씩 재생됨
- 음악은 반드시 처음부터 재생됨
- (음악 길이 < 재생된 길이)인 경우, 음악이 끊김 없이 처음부터 반복해서 재생됨
- (음악 길이 > 재생된 길이)인 경우, 처음부터 재생 시간만큼만 재생됨
- 음악이 00:00를 넘겨서까지 재생되는 일은 없음

<조건이 일치하는 음악이 여러 개인 경우>
- 라디오에서 재생된 시간이 제일 긴 음악 제목을 반환
- 재생된 시간도 같을 경우 먼저 입력된 음악 제목을 반환

<조건이 일치하는 음악이 없는 경우>
- “(None)”을 반환
*/




// 코드 1
function calcMinDifference(start, end) {
    const [startHour, startMin] = start.split(':');
    const [endHour, endMin] = end.split(':');

    return (+endHour * 60 + +endMin) - (+startHour * 60 + +startMin);
}

function findMelody(playedMelody, heardMelody) {
    const re = new RegExp(heardMelody);
    const searchIdx = playedMelody.search(re);
    
    if (searchIdx === -1) return false;
    if (playedMelody[searchIdx + heardMelody.length] === '#') return false;

    return true;
}

function solution(m, musicinfos) {
    const newMusicinfos = [];    
    musicinfos.forEach(info => {
        const [start, end, title, entireMelody] = info.split(',');
        
        const minDiff =  calcMinDifference(start, end);
        const playedMelody = entireMelody
                                .repeat(Math.ceil(minDiff / entireMelody.length))
                                .slice(0, minDiff);
        
        if (findMelody(playedMelody, m)) newMusicinfos.push([minDiff, title, playedMelody]);
    })

    if (newMusicinfos.length === 0) return '(None)';
    if (newMusicinfos.length === 1) return newMusicinfos[0][1];
    return newMusicinfos.reduce(function(acc, cur) {
        const [accMinDiff] = acc;
        const [curMinDiff] = cur;

        if (accMinDiff > curMinDiff) return acc;
        else if (accMinDiff < curMinDiff) return cur;
        else return acc;
    }, newMusicinfos[0])[1];
}

  
// 실행 결과: 실패



// 코드 2
// 참고: https://school.programmers.co.kr/questions/47291
function calcMinDifference(start, end) {
    const [startHour, startMin] = start.split(':');
    const [endHour, endMin] = end.split(':');

    return (+endHour * 60 + +endMin) - (+startHour * 60 + +startMin);
}

function findMelody(playedMelody, heardMelody) {
    const re = new RegExp(heardMelody);
    const searchIdx = playedMelody.search(re);
    
    if (searchIdx === -1) return false;
    if (playedMelody[searchIdx + heardMelody.length] === '#') return false;

    return true;
}

function solution(m, musicinfos) {
    const newMusicinfos = [];   
    const newMelody = m.replace(/(C|D|F|G|A)#/g, (_, p1) => p1.toLowerCase());

    musicinfos.forEach(info => {
        const [start, end, title, entireMelody] = info.split(',');
        
        const newEntireMelody = entireMelody.replace(/(C|D|F|G|A)#/g, (_, p1) => p1.toLowerCase());
        const minDiff =  calcMinDifference(start, end);
        const playedMelody = newEntireMelody
                                .repeat(Math.ceil(minDiff / newEntireMelody.length))
                                .slice(0, minDiff);
        
        if (findMelody(playedMelody, newMelody)) newMusicinfos.push([minDiff, title, playedMelody]);
    })

    if (newMusicinfos.length === 0) return '(None)';
    if (newMusicinfos.length === 1) return newMusicinfos[0][1];
    return newMusicinfos.reduce(function(acc, cur) {
        const [accMinDiff] = acc;
        const [curMinDiff] = cur;

        if (accMinDiff > curMinDiff) return acc;
        else if (accMinDiff < curMinDiff) return cur;
        else return acc;
    }, newMusicinfos[0])[1];
}

// console.log(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
// console.log(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
// console.log(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))

// console.log(solution("ABC", ["12:00,12:06,HELLO,ABC#ABC#ABC"])); // "(None)"
// console.log(solution("ABC", ["12:00,12:10,HELLO,ABC#ABC#ABC"])); // "HELLO"
// console.log(solution("ABC", ["12:04,13:00,HELLO,ABC#ABC#ABC"])); // "HELLO"
// console.log(solution("C#C", ["12:00,12:06,HELLO,C#C#CC#"])); // "HELLO"

  
// 실행 결과: 성공



// 코드 3 - 리팩토링
function calcMinDifference(start, end) {
    const [startHour, startMin] = start.split(':');
    const [endHour, endMin] = end.split(':');

    return (+endHour * 60 + +endMin) - (+startHour * 60 + +startMin);
}

function solution(m, musicinfos) {
    const newMelody = m.replace(/(C|D|F|G|A)#/g, (_, p1) => p1.toLowerCase());

    const answer = musicinfos
        .map(info => {
            const [start, end, title, entireMelody] = info.split(',');
            
            const newEntireMelody = entireMelody.replace(/(C|D|F|G|A)#/g, (_, p1) => p1.toLowerCase());
            const minDiff =  calcMinDifference(start, end);
            const playedMelody = newEntireMelody
                                    .repeat(Math.ceil(minDiff / newEntireMelody.length))
                                    .slice(0, minDiff);
            
            return [minDiff, title, playedMelody];
        })
        .sort((a, b) => b[0] - a[0])
        .filter(([_, $, playedMelody]) => playedMelody.search(new RegExp(newMelody)) !== -1)

    return answer[0] ? answer[0][1] : '(None)';
}


// 실행 결과: 성공