defmodule Exercises.FunctionalSudokuTests do
  use ExUnit.Case
  #doctest Exercises.FunctionalSudoku
  import Exercises.FunctionalSudoku


  @empty_board [
    [nil, nil, nil, nil, nil, nil, nil, nil, nil],
    [nil, nil, nil, nil, nil, nil, nil, nil, nil],
    [nil, nil, nil, nil, nil, nil, nil, nil, nil],
    [nil, nil, nil, nil, nil, nil, nil, nil, nil],
    [nil, nil, nil, nil, nil, nil, nil, nil, nil],
    [nil, nil, nil, nil, nil, nil, nil, nil, nil],
    [nil, nil, nil, nil, nil, nil, nil, nil, nil],
    [nil, nil, nil, nil, nil, nil, nil, nil, nil],
    [nil, nil, nil, nil, nil, nil, nil, nil, nil],

  ]

  @partially_filled_board [
    [nil, nil,   4,   6, nil, nil,   1,   3, nil],
    [  9, nil,   8, nil, nil, nil, nil, nil, nil],
    [  7, nil, nil, nil, nil,   4, nil,   6,   2],
    [nil, nil,   6, nil,   7, nil, nil, nil,   1],
    [nil, nil, nil,   4, nil,   5, nil, nil, nil],
    [  8, nil, nil, nil,   3, nil,   6, nil, nil],
    [  1,   8, nil,   9, nil, nil, nil, nil,   4],
    [nil, nil, nil, nil, nil, nil,   2,   8, nil],
    [nil,   3,   2, nil, nil,   1,   7, nil, nil],

  ]


  test "check_column" do
    assert check_column(@partially_filled_board, 0, 5) == true
    assert check_column(@partially_filled_board, 0, 9) == false
    assert check_column(@partially_filled_board, 2, 9) == true
    assert check_column(@empty_board, 2, 9) == true
    assert check_column(@empty_board, 0, 0) == true
    assert check_column(@partially_filled_board, 8, 1) == false
  end

  test "check_row" do
    assert check_row(@partially_filled_board, 0, 9) == true
    assert check_row(@partially_filled_board, 8, 7) == false
    assert check_row(@partially_filled_board, 7, 1) == true
    assert check_row(@partially_filled_board, 7, 2) == false
  end

  test "check_square" do
    assert check_square(@partially_filled_board, 0, 1) == true
    assert check_square(@partially_filled_board, 1, 1) == true
    assert check_square(@partially_filled_board, 2, 9) == true
    assert check_square(@partially_filled_board, 3, 1) == true
    assert check_square(@partially_filled_board, 4, 1) == true
    assert check_square(@partially_filled_board, 5, 5) == true
    assert check_square(@partially_filled_board, 6, 4) == true
    assert check_square(@partially_filled_board, 7, 8) == true
    assert check_square(@partially_filled_board, 8, 1) == true
    assert check_square(@partially_filled_board, 0, 4) == false
    assert check_square(@partially_filled_board, 1, 6) == false
    assert check_square(@partially_filled_board, 2, 2) == false
    assert check_square(@partially_filled_board, 3, 8) == false
    assert check_square(@partially_filled_board, 4, 3) == false
    assert check_square(@partially_filled_board, 5, 6) == false
    assert check_square(@partially_filled_board, 6, 1) == false
    assert check_square(@partially_filled_board, 7, 9) == false
    assert check_square(@partially_filled_board, 8, 7) == false
  end

  test "check_all" do
    assert check_all(@partially_filled_board, {0, 0}, 2) == true
    assert check_all(@partially_filled_board, {0, 0}, 5) == true
    assert check_all(@partially_filled_board, {0, 0}, 4) == false
    assert check_all(@partially_filled_board, {0, 0}, 7) == false
    assert check_all(@partially_filled_board, {0, 0}, 8) == false
  end

  test "get_valid_numbers" do
    assert get_valid_numbers(@partially_filled_board, {0, 0}) == [2, 5]
    assert get_valid_numbers(@partially_filled_board, {0, 0}, [5]) == [2]
    assert get_valid_numbers(@partially_filled_board, {0, 0}, [2]) == [5]
  end

  test "get_square_number" do
    assert get_square_number(0, 0) == 0
    assert get_square_number(8, 8) == 8
    assert get_square_number(5, 5) == 4
    assert get_square_number(0, 6) == 2
  end


  test "get_value" do
    assert get_value(@partially_filled_board, {0, 2}) == 4
  end

  test "set_value" do
    assert Enum.at(set_value(@partially_filled_board, {0, 0}, 2), 0) == [2, nil,   4,   6, nil, nil,   1,   3, nil]

  end

  test "choose_value" do
    assert choose_value(@partially_filled_board, {0, 0}, [2,5]) == 2

  end

end
