import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:mocktail/mocktail.dart';

import 'package:your_package_name/your_path/empty_list_header.dart';
import 'package:your_package_name/infrastrucutre/bloc/list-bloc/movies_list_bloc.dart';
import 'package:your_package_name/infrastrucutre/bloc/list-bloc/movies_list_state.dart';

// Mock classes
class MockMoviesListBloc extends Mock implements MoviesListBloc {}

class FakeMoviesListState extends Fake implements MoviesListState {}

void main() {
  late MoviesListBloc moviesListBloc;

  setUpAll(() {
    registerFallbackValue(FakeMoviesListState());
  });

  setUp(() {
    moviesListBloc = MockMoviesListBloc();
  });

  testWidgets('shows empty message when Search is empty', (WidgetTester tester) async {
    // Mock the state
    final mockState = MoviesListState(
      moviesList: MoviesListModel(Search: []), // Assuming your model
    );

    when(() => moviesListBloc.state).thenReturn(mockState);
    when(() => moviesListBloc.stream).thenAnswer((_) => Stream.value(mockState));

    await tester.pumpWidget(
      MaterialApp(
        home: BlocProvider<MoviesListBloc>.value(
          value: moviesListBloc,
          child: CustomScrollView(
            slivers: [EmptyListHeader()],
          ),
        ),
      ),
    );

    expect(find.text('Empty movies search history'), findsOneWidget);
  });
}
