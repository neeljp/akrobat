import { Component } from '@angular/core';
import { ApiService } from './api.service';
import { moveItemInArray, transferArrayItem, CdkDragDrop, CdkDragStart, CdkDragEnd, CdkDragEnter, CdkDragExit} from '@angular/cdk/drag-drop';

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

export class TransferItemsListsComponent {
  inactiveExercises = [];

  activeExercises = [];

  drop(event: CdkDragDrop<string[]>){
    if (event.previousContainer === event.container) {
      console.log('dropped Event',
        `> dropped '${event.item.data}' into '${event.container.id}'`);
      moveItemInArray(event.container.data, event.previousIndex, event.currentIndex);
    } else {
      console.log('dropped Event',
        `> dropped '${event.item.data}' into '${event.container.id}'`);
      transferArrayItem(
        event.previousContainer.data,
        event.container.data,
        event.previousIndex,
        event.currentIndex);
    }
  }
  dragStarted(event: CdkDragStart) {
    console.log('dragStarted Event > item', event.source.data);
  }

  dragEnded(event: CdkDragEnd) {
    console.log('dragEnded Event > item', event.source.data);
  }

  dragEntered(event: CdkDragEnter) {
    console.log('dragEntered Event',
      `> dropping '${event.item.data}' into '${event.container.id}'`);
  }

  dragExited(event: CdkDragExit) {
    console.log('dragExited Event',
      `> drag '${event.item.data}' from '${event.container.id}'`);
  }


  constructor(private api: ApiService){
   this.getExercises();
}
  getExercises = () => {
   this.api.getAllExercises().subscribe(
     data => {
      this.inactiveCexercises = data;
  },
  error => {
  console.log(error);
 });
}
}
