import { Injectable } from '@angular/core';
import {MatDialog} from "@angular/material/dialog";
import {ErrorDialogComponent} from "../../components/error-dialog/error-dialog/error-dialog.component";
import {HttpErrorData} from "../../models/error.models";

@Injectable({
  providedIn: 'root'
})
export class ErrorDialogService {
  public isDialogOpen: boolean = false;

  constructor(public dialog: MatDialog) { }

  openDialog(data: HttpErrorData): void  {
    if (this.isDialogOpen) {
      return
    }

    this.isDialogOpen = true;
    const dialogRef = this.dialog.open(ErrorDialogComponent, {
      panelClass: 'error-dialog-panel',
      data: data
    });

    dialogRef.afterClosed().subscribe(result => {
      this.isDialogOpen = false;
    })
  }
}
