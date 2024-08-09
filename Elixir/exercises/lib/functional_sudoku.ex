defmodule Exercises.FunctionalSudoku do
  @size 9

  @empty_board Enum.map(0..(@size-1), fn _ -> Enum.map(0..(@size-1), fn _ -> nil end) end)

  def solve(board \\ @empty_board) do
    case find_empty(board) do
      nil -> {:ok, board}
      {row, col} -> try_numbers(board, row, col, 1..@size)
    end
  end

  defp find_empty(board) do
    Enum.find_value(0..(@size-1), fn row ->
      Enum.find_value(0..(@size-1), fn col ->
        if Enum.at(Enum.at(board, row), col) == nil, do: {row, col}, else: nil
      end)
    end)
  end

  defp try_numbers(board, row, col, range) do
    Enum.reduce_while(range, {:error, board}, fn num, _acc ->
      if valid?(board, row, col, num) do
        new_board = List.update_at(board, row, fn row_content ->
          List.update_at(row_content, col, fn _ -> num end)
        end)

        case solve(new_board) do
          {:ok, solved_board} -> {:halt, {:ok, solved_board}}
          _ -> {:cont, {:error, board}}
        end
      else
        {:cont, {:error, board}}

valid?(board, row, col, num) do
    not Enum.any?(0..(@size-1), fn i ->
      Enum.at(Enum.at(board, row), i) == num or
      Enum.at(Enum.at(board, i), col) == num or
      Enum.at(Enum.at(board, div(row, 3) * 3 + div(i, 3)), div(col, 3) * 3 + rem(i, 3)) == num
    end)
  end
end
