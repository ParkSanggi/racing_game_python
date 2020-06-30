# racing_game_python


1. 기능 요구사항
    1. 주어진 횟수 동안 n대의 자동차는 전진 또는 멈출 수 있다.
    1. 각 자동차에 이름을 부여할 수 있다. 전진하는 자동차를 출력할 때 자동차 이름을 같이 출력한다.
    1. 자동차 이름은 쉼표(,)를 기준으로 구분하며 이름은 5자 이하만 가능하다.
    1. 사용자는 몇 번의 이동을 할 것인지를 입력할 수 있어야 한다.
    1. 전진하는 조건은 0에서 9 사이에서 random 값을 구한 후 random 값이 4 이상일 경우 전진하고, 3 이하의 값이면 멈춘다.
    1. 자동차 경주 게임을 완료한 후 누가 우승했는지를 알려준다. 우승자는 한 명 이상일 수 있다.
    1. car 객체를 활용해 구현해야 한다.
    1. car 기본 생성자를 추가할 수 없다.
    1. name, position 변수의 접근 제어자인 private를 변경할 수 없다.
    1. 가능하면 setPosition(int position) 메소드를 추가하지 않고 구현한다.
    
    public class Car {
        private final String name;
        private int position = 0;

        public Car(String name) {
            this.name = name;
        }
        // 추가 기능 구현
    }
    

1. 기능목록
    1. 사용자에게 자동차들의 이름을 입력받는다. (이름은 쉼표 기준으로 구분)
    1. 사용자로부터 이동 횟수를 입력받는다.

    1. 자동차 이름이 유효한지 확인한다
        1. 자동차 이름이 5자 이하인지 확인한다.
        1. 자동차들에 이름을 부여한다.

    1. 자동차가 전진을 시도한다.
        1. 0에서 9사이의 random 값을 구한다
        1. 랜덤 값이 4이상인 경우 포지션을 증가시킨다.

    1. 실행 결과를 출력한다.
    
    1. 누가 우승했는지 알려준다.
        1. 우승자가 여러명일 경우 모두 알려준다.
