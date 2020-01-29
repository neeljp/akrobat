import { Component } from '@angular/core';
import { ApiService } from './api.service';
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.sass'],
  providers: [ApiService]
})
export class AppComponent {
  title = 'akroread';
  exercises = [{title: 'test'}];
  selectedExercise = [{title: 'test'}];
  constructor(private api: ApiService){
   this.getExercises();
}
 getExercises = () => {
  this.api.getAllExercises().subscribe(
    data => {
     this.exercises = data;
 },
 error => {
 console.log(error);
});
}
 exerciseClicked = (exercise) => {
  this.api.getOneExercise(exercise.id).subscribe(
    data => {
  console.log(data);
  this.selectedExercise = data;
 },
 error => {
 console.log(error);
});


}
}
