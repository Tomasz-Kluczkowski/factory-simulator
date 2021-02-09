import { Injectable } from '@angular/core';
import {MatSnackBar} from '@angular/material/snack-bar';

@Injectable({
  providedIn: 'root'
})
export class NotificationService {

  constructor(private snackbar: MatSnackBar) { }

  showSuccess(message: string): void {
    this.snackbar.open(message, '', {duration: 3000, panelClass: ['notification-service-success']});
  }

  showFailure(message: string): void {
    this.snackbar.open(message, '', {duration: 5000, panelClass: ['notification-service-error']})
  }
}
