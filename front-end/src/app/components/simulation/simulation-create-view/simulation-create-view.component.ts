import { Component, OnInit } from '@angular/core';
import {FormBuilder, Validators} from "@angular/forms";

@Component({
  selector: 'app-simulation-create-view',
  templateUrl: './simulation-create-view.component.html',
  styleUrls: ['./simulation-create-view.component.scss']
})
export class SimulationCreateViewComponent implements OnInit {
  appearance: string = 'standard'

  constructor(private formBuilder: FormBuilder) { }

  ngOnInit(): void {
  }


  factoryConfigForm = this.formBuilder.group({
    requiredItemNames: ['A, B', [Validators.required, Validators.pattern('[a-zA-Z\\s]+(?:,[a-zA-Z\\s]*)*')]],
    productCode: ['P', Validators.required],
    emptyCode: ['E', Validators.required],
    numberOfSimulationSteps: ['10', [Validators.min(1), Validators.required]],
    numberOfConveyorBeltSlots: ['3', [Validators.min(1), Validators.required]],
    numberOfWorkerPairs: ['3', [Validators.min(1), Validators.required]],
    pickupTime: ['1', [Validators.min(1), Validators.required]],
    dropTime: ['1', [Validators.min(1), Validators.required]],
    buildTime: ['4', [Validators.min(1), Validators.required]],
  })

  onSubmit() {
    console.warn(this.factoryConfigForm.value);
    let requiredItemNames = this.factoryConfigForm.value.requiredItemNames;
    console.log(requiredItemNames);
    requiredItemNames = requiredItemNames.replace(/,/g, ' ');
    console.log(requiredItemNames);
    let requiredItemNamesArray = requiredItemNames.split(' ');

    const output = [];
    for (let item of requiredItemNamesArray) {
      const cleanItem = item.split(' ').join('');
      if (cleanItem !== '') {
        output.push(cleanItem)
      }
    }

    // TODO: before patching the value to show what we really care about we have to call the api and try to post.

    this.factoryConfigForm.patchValue({
      requiredItemNames: output.join(', ')
    })
    console.log(output)
  }

  isControlInvalid(controlName: string): boolean {
    return this.factoryConfigForm.get(controlName).invalid;
  }

  getRequiredItemNamesErrorMessage(): string {
    let message = 'This field is required';
    if (this.factoryConfigForm.get('requiredItemNames').hasError('pattern')) {
      message = 'Only letters, commas and spaces are allowed';
    }

    return message;
  }
}
