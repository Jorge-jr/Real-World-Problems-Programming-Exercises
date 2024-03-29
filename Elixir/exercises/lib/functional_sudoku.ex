defmodule Exercises.FunctionalSudoku do
  @moduledoc """
  This module provides functions to solve Sudoku puzzles using functional programming. Aditionally, providing an empty board will create a new one to be solved.

  ## Examples

  ```elixir
  iex> board = [
  ...>   [5, 3, nil, nil, 7, nil, nil, nil, nil],
  ...>   [6, nil, nil, 1, 9, 5, nil, nil, nil],
  ...>   [nil, 9, 8, nil, nil, nil, nil, 6, nil],
  ...>   [8, nil, nil, nil, 6, nil, nil, nil, 3],
  ...>   [4, nil, nil, 8, nil, 3, nil, nil, 1],
  ...>   [7, nil, nil, nil, 2, nil, nil, nil, 6],
  ...>   [nil, 6, nil, nil, nil, nil, 2, 8, nil],
  ...>   [nil, nil, nil, 4, 1, 9, nil, nil, 5],
  ...>   [nil, nil, nil, nil, 8, nil, nil, 7, 9]
  ...> ]
  ...> Exercises.FunctionalSudoku.fill_board(board)
"""

  def fill_board(board\\@empty_board), do: do_fill_board(board, {0, 0})

  defp do_fill_board(board, {9, _}), do: {:ok, board}
  defp do_fill_board(board, {row, 9}), do: do_fill_board(board, {row+1, 0})
  defp do_fill_board(board, {row, 9}, exclude), do: do_fill_board(board, {row+1, 0})
  defp do_fill_board(board, {row, column}, exclude\\[]) do
    value = choose_value(board, {row, column}, Enum.shuffle(get_valid_numbers(board, {row, column})))
    if :no_valid_numbers == value do
      {:error, exclude ++ [get_value(board, {row, column-1})]}
    else
      case do_fill_board(set_value(board, {row, column}, value), {row, column+1}) do
        {:ok, new_board} -> {:ok, new_board}
        {:error, new_exclude} ->
          case choose_value(board, {row, column}, Enum.shuffle(get_valid_numbers(board, {row, column}, new_exclude))) do
            :no_valid_numbers -> {:error, exclude ++ [get_value(board, {row, column-1})]}
            new_value -> do_fill_board(set_value(board, {row, column}, new_value), {row, column+1})
          end
      end
    end
  end

  def get_square_number(row, column), do: (3*(trunc(row/3))) + (trunc(column/3))

  def check_row(board, index, value), do: value not in Enum.at(board, index)

  def check_column(_, index, _) when index > 8 , do: true
  def check_column(board, index, value) do
    value not in for row <- 0..8, do: Enum.at(Enum.at(board, row), index)
  end

  def check_square(_board, square_number, _) when square_number > 8, do: true
  def check_square(board, square_number, value) do
    starting_row = 3 * (trunc(square_number/3))
    starting_column = 3 * (rem(square_number, 3))
    indexes = for row <- [starting_row,starting_row+1,starting_row+2], column <- [starting_column,starting_column+1,starting_column+2], do: {row, column}
    value not in for entry <- indexes, do: Enum.at(Enum.at(board, elem(entry, 0)), elem(entry, 1))
  end

  def check_all(board, {row, column}, value), do: check_row(board, row, value) and check_column(board, column, value) and check_square(board, get_square_number(row, column), value)

  def get_valid_numbers(board, {row, column}), do: for x <- 1..9, check_all(board, {row, column}, x), do: x
  def get_valid_numbers(board, {row, column}, exclude), do: for x <- 1..9, check_all(board, {row, column}, x) and x not in exclude, do: x

  def get_value(board, {row, column}), do: Enum.at(Enum.at(board, row), column)

  def set_value(board, {row, column}, value), do: List.replace_at(board, row, List.replace_at(Enum.at(board, row), column, value))

  def choose_value(_board, {_row, _column}, []), do: :no_valid_numbers
  def choose_value(board, {row, column}, [head|tail]) do
    cond do
      column == 8 -> head
      get_valid_numbers(set_value(board, {row, column}, head), {row, column+1}) == [] -> choose_value(board, {row, column}, tail)
      true -> head
    end
  end
end
