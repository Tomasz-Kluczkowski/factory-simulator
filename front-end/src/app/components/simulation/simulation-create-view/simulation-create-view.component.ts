import { Component, OnInit } from '@angular/core';
import {FormControl, FormGroup, Validators} from "@angular/forms";

@Component({
  selector: 'app-simulation-create-view',
  templateUrl: './simulation-create-view.component.html',
  styleUrls: ['./simulation-create-view.component.scss']
})
export class SimulationCreateViewComponent implements OnInit {
  appearance: string = 'standard'

  constructor() { }

  ngOnInit(): void {
  }


  factoryConfigForm = new FormGroup({
    requiredItemNames: new FormControl('A, B', Validators.required),
    productCode: new FormControl('P', Validators.required),
    emptyCode: new FormControl('E', Validators.required),
    numberOfSimulationSteps: new FormControl('10', [Validators.min(1), Validators.required] ),
    numberOfConveyorBeltSlots: new FormControl('3', [Validators.min(1), Validators.required]),
    numberOfWorkerPairs: new FormControl('3', [Validators.min(1), Validators.required]),
    pickupTime: new FormControl('1', [Validators.min(1), Validators.required]),
    dropTime: new FormControl('1', [Validators.min(1), Validators.required]),
    buildTime: new FormControl('4', [Validators.min(1), Validators.required]),
  })

  onSubmit() {
    console.warn(this.factoryConfigForm.value);
  }

  isControlInvalid(controlName: string): boolean {
    return this.factoryConfigForm.get(controlName).invalid;
  }

}
